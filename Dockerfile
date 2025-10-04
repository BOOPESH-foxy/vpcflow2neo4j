FROM neo4j:latest
EXPOSE 7474 7473 7687
VOLUME ["/data", "/logs", "/import", "/plugins"]
