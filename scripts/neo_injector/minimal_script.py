#!/usr/bin/env python3
import os
import orjson as json
from neo4j import GraphDatabase

NEO4J_URI = os.getenv("NEO4J_URI", "neo4j://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "please-change")
GRAPH_JSON = os.getenv("GRAPH_JSON", "Graphs/graph.json")

CREATE_UNIQUE_CONSTRAINT = """
CREATE CONSTRAINT resource_id IF NOT EXISTS
FOR (n:Resource) REQUIRE n.id IS UNIQUE
"""

UPSERT_NODES = """
UNWIND $nodes AS n
MERGE (x:Resource {id: n.id})
SET x += n.props
WITH x, n
CALL apoc.create.addLabels(x, [n.label]) YIELD node
RETURN count(*) AS upserted
"""

UPSERT_RELS = """
UNWIND $rels AS r
MATCH (a:Resource {id: r.src}), (b:Resource {id: r.dst})
WITH a, b, r
CALL apoc.create.relationship(a, r.type, r.props, b) YIELD rel
RETURN count(rel) AS linked
"""

def load_graph(path):
    with open(path, "rb") as f:
        data = json.loads(f.read())
    nodes = [
        {"id": n["id"],
         "label": n["type"],
         "props": {k: v for k, v in n.items() if k not in ("id", "type")}}
        for n in data.get("nodes", [])
    ]
    rels = [
        {"src": e["src"], "dst": e["dst"], "type": e["kind"],
         "props": {k: v for k, v in e.items() if k not in ("src", "dst", "kind")}}
        for e in data.get("edges", [])
    ]
    return nodes, rels

def main():
    if not os.path.exists(GRAPH_JSON):
        raise FileNotFoundError(f"Missing {GRAPH_JSON}")
    nodes, rels = load_graph(GRAPH_JSON)
    print(f"Graph: {len(nodes)} nodes, {len(rels)} relationships")

    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
    with driver.session() as s:
        s.run(CREATE_UNIQUE_CONSTRAINT).consume()
        if nodes:
            s.run(UPSERT_NODES, nodes=nodes).consume()
        if rels:
            s.run(UPSERT_RELS, rels=rels).consume()
    driver.close()
    print("Ingest complete.")

if __name__ == "__main__":
    main()
