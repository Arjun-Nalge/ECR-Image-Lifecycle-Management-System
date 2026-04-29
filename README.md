# 🧹 Automated Docker Image Cleanup using AWS ECR

## 📌 Overview

This project automates the cleanup of unused and old Docker images stored in Amazon ECR using AWS Lambda and scheduled triggers from Amazon CloudWatch.

It helps reduce storage costs, removes stale container images, and keeps the container registry optimized.

---

## 🏗️ Architecture

```
          +----------------------+
          |  CloudWatch Events   |
          |  (Scheduled Trigger) |
          +----------+-----------+
                     |
                     v
          +----------------------+
          |     AWS Lambda       |
          |  (Cleanup Function)  |
          +----------+-----------+
                     |
                     v
          +----------------------+
          |     Amazon ECR       |
          | (Container Registry) |
          +----------------------+
                     |
                     v
          +----------------------+
          |  CloudWatch Logs     |
          +----------------------+
```

---

## ⚙️ Features

* Deletes untagged or old Docker images
* Fully serverless automation
* Scheduled cleanup (daily/weekly)
* Reduces ECR storage costs
* Logging and monitoring support

---

## 🛠️ Tech Stack

* Amazon ECR
* AWS Lambda
* Amazon CloudWatch
* AWS IAM
* Python (Boto3)
* Docker

---

## 🚀 Setup Instructions

### 1. Create ECR Repository

* Go to AWS Console → ECR
* Create a repository (e.g., `image-cleanup-repo`)
* Push Docker images:

```bash
docker build -t my-app .
docker tag my-app:latest <account-id>.dkr.ecr.<region>.amazonaws.com/image-cleanup-repo
docker push <account-id>.dkr.ecr.<region>.amazonaws.com/image-cleanup-repo
```

---

### 2. Create IAM Role for Lambda

Attach the ECR permissions (IAM/policy.json)
Also add logging permissions:

* logs:CreateLogGroup
* logs:CreateLogStream
* logs:PutLogEvents

---

### 3. Create Lambda Function

* Runtime: Python 3.x
* Attach IAM Role
* Add the Python code. (lambda/cleanup.py)

---

### 4. Create CloudWatch Schedule

* Go to CloudWatch → Rules
* Create rule:

  * Type: Schedule
  * Example: `rate(1 day)`
* Attach Lambda function

---

### 5. Testing

* Push multiple Docker images (tagged & untagged)
* Trigger Lambda manually
* Check CloudWatch logs
* Verify old/unused images are deleted

---

## 📂 Project Structure

```
ecr-image-cleanup/
│
├── lambda/
│   └── cleanup.py
│
├── iam/
│   └── policy.json
│
├── docker/
│   └── Dockerfile
│
└── README.md
```

---

## 🧪 Example Scenario

| Image Tag | Age (Days) | Result  |
| --------- | ---------- | ------- |
| latest    | 5          | Kept    |
| v1        | 40         | Deleted |
|           | 10         | Deleted | (untagged)

---

## Author
Arjun Nalge - DevOps Engineer

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](https://www.linkedin.com/in/arjun-nalge-313642398)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?logo=github)](https://github.com/Arjun-Nalge/Arjun-Nalge.git)
