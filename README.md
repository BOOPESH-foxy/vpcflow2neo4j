# vpcflow-neo4j

Collect **AWS VPC Flow Logs** with **boto3** and explore relationships in **Neo4j**.

> Pulls flow logs from **CloudWatch Logs** or **S3** and writes a graph you can query/visualize in Neo4j.

---

## Status
Early initial commit. Interfaces may change.

## Features (initial scope)
- Sources: **CloudWatch Logs** *or* **S3 (.gz)**
- Neo4j graph model

---

## Requirements
- Python **3.10+**
- AWS account with **VPC Flow Logs** enabled (destination: CloudWatch Logs or S3)
- Neo4j **5.x** (local Docker or Aura)
- AWS credentials via `AWS_PROFILE`, env vars, or IAM role

---

## Quickstart

### 1. Setup
```bash
pip install -r requirements.txt
