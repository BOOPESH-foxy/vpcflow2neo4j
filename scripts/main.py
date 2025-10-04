import os
import typer
from aws_vpc import check_vpc_existence,create_vpc

app = typer.Typer(help="FETCH VPC FLOW LOGS FROM S3,CloudWatch")

@app.command("check_vpc")
def check_vpc(name: str):
    "Checks for the vpc existence to fetch the flow logs"
    check_vpc_existence(name)

@app.command("create_vpc")
def check_vpc(name: str):
    "Creates the vpc"
    create_vpc(name)

if __name__ == "__main__":
    app()