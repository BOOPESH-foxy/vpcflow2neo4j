from tqdm import tqdm
from aws_region import fetch_regions
from aws_session import boto3_session
from aws_data_functions import collect_region_data
from concurrent.futures import ThreadPoolExecutor, as_completed

def main():
    import argparse
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("--name", help="If not provided, uses the account as the folder name to store resources")
    argument_parser.add_argument("--account", required=True)
    argument_parser.add_argument("--regions", nargs="*", help="If not provided, discovers all the regions in Account")
    args = argument_parser.parse_args()
    session = boto3_session()
    regions_list =  args.regions or fetch_regions()
        
    with ThreadPoolExecutor(max_workers=8) as executor:
        data_collection_progress = [executor.submit(collect_region_data,session,_,args.account,name=args.name) for _ in regions_list]
        for _ in tqdm(as_completed(data_collection_progress), total=len(data_collection_progress), desc="Collected"):
            pass
    

if __name__ == "__main__":
    main()