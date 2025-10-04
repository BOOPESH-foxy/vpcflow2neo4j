import os
import typer
from aws_vpc import fetch_vpc_id

app = typer.Typer(help="FETCH VPC FLOW LOGS FROM S3,CloudWatch")

@app.command("check_vpc")
def fetch_vpc_id(name: str):
    "Checks for the vpc existence to fetch the flow logs"
    fetch_vpc_id(name)

@app.command("create_vpc")
def check_vpc(name: str):
    "Creates the vpc"

if __name__ == "__main__":
    app()