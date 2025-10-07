import os
import orjson as json
import botocore

def pagination_result(client,resource_operation, key):
    response_pagination = client.get_paginator(resource_operation)
    for _ in response_pagination.paginate():
        for item in _.get(key, []):
            yield item

def write_json_data(file,data):
    os.makedirs(os.path.dirname(file), exist_ok=True)
    with open(file, "wb") as file_write:
        file_write.write(json.dumps(data))

def collect_region_data(session,region,account,name=None):
    ec2 = session.client("ec2",region_name=region)
    outdir = f"Output/{name or account}/{region}"

    vpcs        = list(pagination_result(ec2, "describe_vpcs", "Vpcs"))
    route_table = list(pagination_result(ec2, "describe_route_tables", "RouteTables"))
    subnets     = list(pagination_result(ec2, "describe_subnets", "Subnets"))
    enis        = list(pagination_result(ec2, "describe_network_interfaces", "NetworkInterfaces"))
    sgs         = list(pagination_result(ec2, "describe_security_groups", "SecurityGroups"))
    igw         = list(pagination_result(ec2, "describe_internet_gateways", "InternetGateways"))
    natGateway  = list(pagination_result(ec2, "describe_nat_gateways", "NatGateways"))
    vpcEndpoint = list(pagination_result(ec2, "describe_vpc_endpoints", "VpcEndpoints"))
    vpcPeering  = list(pagination_result(ec2, "describe_vpc_peering_connections", "VpcPeeringConnections"))
    NetworkACLs = list(pagination_result(ec2, "describe_network_acls", "NetworkAcls"))

    try:
        tgw             = list(pagination_result(ec2, "describe_transit_gateways", "TransitGateways"))
        tgwAttachments  = list(pagination_result(ec2, "describe_transit_gateway_attachments", "TransitGatewayAttachments"))

    except botocore.exceptions.ClientError:
        tgw, tgwAttachments = [], []

    for resource,data in [
        ("vpcs", vpcs), ("subnets", subnets), ("enis", enis), ("sgs", sgs),("route_tables",route_table),
        ("igw", igw), ("nat_gateways", natGateway), ("vpc_endpoints", vpcEndpoint),
        ("peering", vpcPeering), ("nacls", NetworkACLs), ("tgw", tgw), ("tgw_attachments", tgwAttachments),
        
    ]:
        write_json_data(f"{outdir}/{resource}.json", data)
        
    return region
