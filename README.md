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
* Push Docker images.

---

### 2. Create IAM Role for Lambda

Attach the Required Permissions.
Also add logging permissions:

* logs:CreateLogGroup
* logs:CreateLogStream
* logs:PutLogEvents

---

### 3. Create Lambda Function

* Runtime: Python 3.14
* Attach IAM Role
* Add the Python code

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
