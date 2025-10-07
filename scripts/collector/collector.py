import os
import boto3
import botocore
from tqdm import tqdm
from aws_session import aws_session
# from aws_vpc import fetch_vpc_ids
from aws_region import fetch_regions


Name = ""
Region = ""
session = aws_session()

output_directory = f"Output/{Name}/{Region}"


def collect_region_data(region,account):
    print(region,account)


def main():
    import argparse
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("--account", required=True)
    argument_parser.add_argument("--regions", nargs="*", help="If not provided, discovers all the regions in Account")
    args = argument_parser.parse_args()

    regions_list =  args.regions or fetch_regions()

    data_collection_progress = [collect_region_data(regions_list[_],args.account) for _ in range(len(regions_list))]

if __name__ == "__main__":
    main()