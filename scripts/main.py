import os
import typer
from scripts.collector.aws_region import fetch_regions

app = typer.Typer(help="FETCH VPC FLOW LOGS FROM S3,CloudWatch")

@app.command("fetch_vpc_ids")
def fetch_vpc_ids_typer():
    "Fetch VPC's in each regions"

@app.command("fetch_regions")
def fetch_regions_typer():
    "Fetches regions"
    fetch_regions()

if __name__ == "__main__":
    app()