

def pagination_result(client,resource_operation, key):
    response_pagination = client.get_paginator(resource_operation)
    for _ in response_pagination.paginate():
        for item in _.get(key, []):
            yield item


def create_folder(Name,Region):
    output_directory = f"Output/{Name}/{Region}"


def collect_region_data(session,region,account):
    print("in collect region data")
    ec2 = session.client("ec2",region_name=region)
    create_folder(account,region)

    vpcs   = list(pagination_result(ec2, "describe_vpcs", "Vpcs"))
    subnets= list(pagination_result(ec2, "describe_subnets", "Subnets"))
    enis   = list(pagination_result(ec2, "describe_network_interfaces", "NetworkInterfaces"))
    sgs    = list(pagination_result(ec2, "describe_security_groups", "SecurityGroups"))
    igw    = list(pagination_result(ec2, "describe_internet_gateways", "InternetGateways"))
    natGateway  = list(pagination_result(ec2, "describe_nat_gateways", "NatGateways"))
    vpcEndpoint   = list(pagination_result(ec2, "describe_vpc_endpoints", "VpcEndpoints"))
    vpcPeering   = list(pagination_result(ec2, "describe_vpc_peering_connections", "VpcPeeringConnections"))
    NetworkACLs  = list(pagination_result(ec2, "describe_network_acls", "NetworkAcls"))