# 🚀 Automated Daily Payment Reporting System

## 📋 **Project Overview**
This project is an automated solution using AWS services to generate and store daily payment reports efficiently. The system integrates multiple AWS services to create a robust and scalable reporting mechanism. 

---

## 🛠️ **Features**
- 🌅 **Automated daily report generation** at 8:00 AM
- 📊 Retrieves payment data from **RDS MySQL** database
- 📝 Generates **PDF reports** of previous day's payments
- ☁️ Stores reports in **S3 bucket**
- ⚡ Uses **AWS Lambda** for serverless computing
- 🗓️ Implements **EventBridge** for scheduling
- 🔐 Secure **IAM user** configuration

---

## 💻 **Technologies Used**

### AWS Services:
- 🗃️ **RDS (MySQL Database)**
- ⚙️ **Lambda**
- 🛢️ **S3**
- 📅 **EventBridge (CloudWatch Events)**
- 🛡️ **IAM**

### Programming Languages:
- 🐍 **Python 3.9**
- 🧮 **SQL**

---

## 🔑 **Key Components**

### 🗃️ **Database**
- MySQL database hosted on **AWS RDS**.
- Stores payment information including:
  - 👤 **Name**
  - 👥 **Surname**
  - 🆔 **ID Number**
  - 💵 **Payment Amount**
  - 📅 **Payment Date**

### ⚙️ **Lambda Function**
- 📈 Generates daily payment reports.
- 🔍 Queries previous day's payments.
- 📄 Creates **PDF** with total payments and record count.
- ☁️ **Uploads** report to **S3 bucket**.

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
