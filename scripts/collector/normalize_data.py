import os, glob, orjson as json

def load(p): 
    with open(p, "rb") as f: return json.loads(f.read())

def name_from_tags(tags): 
    return next((t["Value"] for t in (tags or []) if t.get("Key")=="Name"), None)

def normalize(account_root):
    nodes, edges = [], []
    acct = os.path.basename(account_root)

    def N(t, id_, **attrs):
        nodes.append({"type": t, "id": id_, **attrs}); return id_
    def E(src, dst, kind, **attrs):
        edges.append({"src": src, "dst": dst, "kind": kind, **attrs})

    for region_dir in sorted(glob.glob(os.path.join(account_root, "*"))):
        if not os.path.isdir(region_dir): continue
        region = os.path.basename(region_dir)
        rid = N("Region", f"region:{region}", name=region)

        vpcs = load(os.path.join(region_dir, "vpcs.json"))
        vpc_ids = {}
        for v in vpcs:
            vid = f"vpc:{v['VpcId']}"
            vpc_ids[v["VpcId"]] = vid
            N("VPC", vid, cidr=v.get("CidrBlock"), name=name_from_tags(v.get("Tags")), region=region)
            E(rid, vid, "HAS_VPC")

        subs = load(os.path.join(region_dir, "subnets.json"))
        for s in subs:
            sid = f"subnet:{s['SubnetId']}"
            N("Subnet", sid, cidr=s.get("CidrBlock"), az=s.get("AvailabilityZone"), name=name_from_tags(s.get("Tags")))
            E(vpc_ids[s["VpcId"]], sid, "HAS_SUBNET")

        enis = load(os.path.join(region_dir, "enis.json"))
        for n in enis:
            nid = f"eni:{n['NetworkInterfaceId']}"
            ips = [n.get("PrivateIpAddress")] + [p["PrivateIpAddress"] for p in n.get("PrivateIpAddresses",[])]
            N("ENI", nid, ips=",".join([i for i in ips if i]))
            if n.get("SubnetId"):
                E(f"subnet:{n['SubnetId']}", nid, "HAS_ENI")

        igws = load(os.path.join(region_dir, "igw.json"))
        for i in igws:
            igid = f"igw:{i['InternetGatewayId']}"
            N("InternetGateway", igid)
            for a in i.get("Attachments", []):
                if a.get("VpcId"):
                    E(vpc_ids[a["VpcId"]], igid, "ATTACHED_IGW")

        natgws = load(os.path.join(region_dir, "nat_gateways.json"))
        nat_index = {}
        for ng in natgws:
            nid = f"nat:{ng['NatGatewayId']}"
            nat_index[ng["NatGatewayId"]] = nid
            N("NatGateway", nid, state=ng.get("State"))

        rts = load(os.path.join(region_dir, "route_tables.json"))
        for rt in rts:
            rtid = f"rt:{rt['RouteTableId']}"
            N("RouteTable", rtid)
            if rt.get("VpcId"): E(vpc_ids[rt["VpcId"]], rtid, "HAS_RT")
            for a in rt.get("Associations", []):
                if a.get("SubnetId"):
                    E(f"subnet:{a['SubnetId']}", rtid, "ASSOCIATED_RT")
            for r in rt.get("Routes", []):
                if r.get("DestinationCidrBlock") == "0.0.0.0/0":
                    if "GatewayId" in r and str(r["GatewayId"]).startswith("igw-"):
                        E(rtid, f"igw:{r['GatewayId']}", "DEFAULT_TO", dest="0.0.0.0/0")
                    if "NatGatewayId" in r:
                        E(rtid, f"nat:{r['NatGatewayId']}", "DEFAULT_TO", dest="0.0.0.0/0")

    os.makedirs("Graphs", exist_ok=True)
    with open("Graphs/graph.json","wb") as f:
        f.write(json.dumps({"nodes": nodes, "edges": edges}))
    print(f"Normalized → Graphs/graph.json  nodes={len(nodes)} edges={len(edges)}")

if __name__ == "__main__":
    # change this to your actual output root
    normalize("Output/boo-foxy")
