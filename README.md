<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Poppins&size=32&duration=2200&pause=900&color=00C853&center=true&vCenter=true&width=700&lines=AWS+Payment+Reporting+System;Automated+%E2%80%A2+Scalable+%E2%80%A2+Secure!" alt="Payment Reporting" />

<br/>

<img src="https://img.shields.io/badge/AWS-Payment%20Automation-00C853?style=for-the-badge&logo=amazonaws&logoColor=white" alt="AWS"/>
<img src="https://img.shields.io/badge/Lambda-Serverless-FF9900?style=for-the-badge&logo=aws-lambda&logoColor=white" alt="Lambda"/>
<img src="https://img.shields.io/badge/MySQL-Database-00758F?style=for-the-badge&logo=mysql&logoColor=white" alt="MySQL"/>
<img src="https://img.shields.io/badge/Python-3.9-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>

<br/><br/>

## ✨ Intelligent Payment Processing Platform

**An enterprise-grade solution for automated daily payment reporting using AWS cloud services**

🌐 *Automate • Track • Report* 

</div>

---

## 🎯 **Project Overview**

This cutting-edge platform delivers automated daily payment reporting with enterprise-level reliability. Built on AWS infrastructure, it seamlessly integrates multiple services to process, analyze, and archive payment data in real-time.

**Key Highlight:** Reports are automatically generated and stored daily at 8:00 AM ☀️

---

## ✨ **Core Features**

<div align="center">

| Feature | Description |
|---------|-------------|
| 🌅 **Automated Scheduling** | Daily report generation at 8:00 AM via EventBridge |
| 📊 **Real-time Data Retrieval** | Direct integration with RDS MySQL database |
| 📄 **PDF Generation** | Professional report formatting with payment summaries |
| ☁️ **Cloud Storage** | Secure archival in S3 bucket |
| ⚡ **Serverless Architecture** | Scalable Lambda functions, zero maintenance |
| 🔐 **Enterprise Security** | IAM role-based access control |

</div>

---

## 🚀 **Technology Stack**

<div align="center">

![AWS](https://img.shields.io/badge/AWS-Cloud%20Platform-FF9900?style=flat-square&logo=amazonaws&logoColor=white)
![Lambda](https://img.shields.io/badge/Lambda-Compute-FF9900?style=flat-square&logo=aws-lambda&logoColor=white)
![RDS](https://img.shields.io/badge/RDS-MySQL%20Database-527FFF?style=flat-square&logo=amazon-rds&logoColor=white)
![S3](https://img.shields.io/badge/S3-Storage-569A31?style=flat-square&logo=amazon-s3&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.9-3776AB?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-000000?style=flat-square&logo=flask&logoColor=white)

</div>

---

## 📊 **System Architecture**

### AWS Services Integration:
- 🗃️ **RDS (MySQL)** — Reliable database with payment records
- ⚙️ **Lambda** — Serverless functions for report generation
- 🛢️ **S3** — Scalable cloud storage for reports
- 📅 **EventBridge** — Intelligent scheduling and automation
- 🛡️ **IAM** — Secure role-based access management

### Backend Stack:
- 🐍 **Python 3.9** — Core application logic
- 🧮 **SQL** — Database queries
- 🌐 **Flask** — Web framework
- 📦 **PyMySQL** — Database connector

---

## 🔑 **Core System Components**

### 🗃️ **Database (RDS MySQL)**
The robust MySQL database stores comprehensive payment information:
- 👤 **Full Name** — Cardholder name
- 👥 **Surname** — Extended identification
- 🆔 **Cedula (ID Number)** — Unique identifier
- 💵 **Payment Amount (Valor_Pagos)** — Transaction value
- 📅 **Consignment Date** — Payment timestamp

### ⚙️ **Lambda Function**
Intelligent serverless processor that:
- 📈 Generates daily payment reports automatically
- 🔍 Queries previous day's complete payment data
- 📄 Creates professional PDF documents
- ☁️ Uploads reports securely to S3 bucket

### 🔄 **Automation**
- 🕗 Triggered daily at **8:00 AM** using **EventBridge**.
- 🕹️ Uses **cron expression** for scheduling.

---

## ⚡ **Setup Requirements**
- 📌 **AWS Account**
- 🐍 **Python 3.9+**
- 🖥️ **MySQL Workbench**
- 💻 **AWS CLI**
- 📚 Required Python libraries:
  - `pymysql`
  - `fpdf`
  - `boto3`

---

## 🔒 **Security Considerations**
- 🔑 Implemented **IAM user** with least privilege access.
- 🛑 **S3 bucket** access carefully configured.
- 🚫 Public access to resources **blocked**.

---

## 🚀 **Deployment Steps**
1. 🗄️ Create **RDS MySQL Database**.
2. ☁️ Set up **S3 Bucket**.
3. ⚙️ Configure **Lambda Function**.
4. 🧑‍💻 Create **IAM User**.
5. 📅 Set up **EventBridge Trigger**.

---

## 🤝 **Contributions**
Contributions are welcome! Please fork the repository and submit a pull request. 🙌



## 🌟 **Acknowledgments**
Project completed for myself.

---

## ✍️ **Author**
Made with ❤️ by **Andrés Fábregas** (ANDFS2411x) 🌱
