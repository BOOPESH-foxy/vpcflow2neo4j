# vpcflow-neo4j

Collect **AWS VPC Flow Logs** with **boto3** and explore relationships in **Neo4j**.

> Pulls flow logs from **CloudWatch Logs** or **S3** for a user specified VPC and writes a graph you can query/visualize in Neo4j.

---

## Status
Boto3 setup for collecting logs - Under development. 

## Features (initial scope)
- Create **VPC Flow Logs**(destination: CloudWatch Logs and S3 - as per user requirement)
- Download flow logs from the user specified flow log
- Sources: **CloudWatch Logs** *and* **S3 (.gz)**
- Neo4j graph model

---

## Requirements
- Python **3.10+**
- AWS account 
- Neo4j **5.x** (local Docker)
- AWS credentials via `IAM role`

---

## Quickstart

### 1. Setup
```bash
git clone https://github.com/BOOPESH-foxy/vpcflow2neo4j.git