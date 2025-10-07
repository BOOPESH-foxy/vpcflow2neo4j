import os
import time
from tqdm import tqdm
from aws_region import fetch_regions
from aws_vpc import fetch_vpc_ids

Name = ""
Region = ""

output_directory = f"Output/{Name}/{Region}"


def main():
    import argparse
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("--account", required=True)
    argument_parser.add_argument("--regions", nargs="*", help="If not provided, discovers all the regions in Account")
    args = argument_parser.parse_args()