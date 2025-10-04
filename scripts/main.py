import os
import typer
from aws_vpc import fetch_vpc_ids
from aws_region import fetch_regions

app = typer.Typer(help="FETCH VPC FLOW LOGS FROM S3,CloudWatch")

@app.command("fetch_vpc_ids")
def fetch_vpc_ids_typer():
    "Fetch VPC's in each regions"
    fetch_vpc_ids()

@app.command("fetch_regions")
def fetch_regions_typer():
    "Fetches regions"
    fetch_regions()
    

if __name__ == "__main__":
    app()