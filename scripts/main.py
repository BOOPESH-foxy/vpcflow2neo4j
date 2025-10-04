import os
import typer
from aws_vpc import fetch_vpc_ids

app = typer.Typer(help="FETCH VPC FLOW LOGS FROM S3,CloudWatch")

@app.command("fetch_vpc_ids")
def fetch_vpc_ids_typer():
    "Checks for the vpc existence to fetch the flow logs"
    fetch_vpc_ids()

@app.command("fetch_subnet_ids")
def check_vpc():
    "Fetches subnets associated with VPC"
    pass

if __name__ == "__main__":
    app()