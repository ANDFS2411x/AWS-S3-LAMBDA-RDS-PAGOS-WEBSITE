<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Poppins&size=36&duration=2200&pause=900&color=10B981&center=true&vCenter=true&width=900&lines=AWS+Payment+Dashboard;Automated+Serverless+Reporting;Lambda+%E2%80%A2+RDS+%E2%80%A2+S3+%E2%80%A2+Flask" alt="AWS Payment Dashboard" />

<br/>

<img src="https://img.shields.io/badge/AWS-Cloud%20Architecture-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white" alt="AWS Services"/>
<img src="https://img.shields.io/badge/Flask-Web%20Dashboard-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask"/>
<img src="https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
<img src="https://img.shields.io/badge/MySQL-Database-4479A1?style=for-the-badge&logo=mysql&logoColor=white" alt="MySQL"/>

<br/>

<img src="https://img.shields.io/badge/Status-Active%20Development-success?style=flat-square" alt="Status"/>
<img src="https://img.shields.io/badge/License-MIT-blue?style=flat-square" alt="License"/>

<br/><br/>

</div>

---

<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Poppins&size=18&duration=3000&pause=1000&color=10B981&center=true&vCenter=true&width=600&lines=Serverless+Payment+Management;Automated+Reports+%26+Real-time+Tracking" alt="AWS Dashboard" />

<br/>

**A powerful serverless payment management system combining AWS Cloud Services with a modern, interactive web dashboard for real-time payment tracking and automated report generation.**

💰 *Automated • Scalable • Serverless • Real-time* 

</div>

---

## ✨ Key Features

💚 **Fully Automated Reports** — Scheduled daily payment generation at 8:00 AM using EventBridge  
📊 **Real-time Web Dashboard** — Interactive Flask interface for live payment tracking  
⚡ **AWS Lambda Processing** — Serverless PDF report generation with zero infrastructure overhead  
🗄️ **MySQL RDS Storage** — Secure relational database with comprehensive payment records  
☁️ **S3 Cloud Storage** — Automatic report archival with pre-signed secure downloads  
🔄 **Complete CRUD Operations** — Add, view, update, and delete payment transactions  
🔐 **Enterprise Security** — IAM roles, least privilege access, and secure credential management  
📱 **Responsive UI** — Beautiful, modern web interface accessible on all devices  

---

## 🏗️ System Architecture

This project integrates multiple AWS services into a cohesive, serverless payment management ecosystem:

```
AWS Cloud Ecosystem
├── EventBridge (Daily Scheduler - 8:00 AM)
│   └── Lambda Function (PDF Report Generation)
│       └── S3 (Report Archive & Storage)
│
├── RDS MySQL (Payment Database)
│   ├── Payment Records
│   ├── User Information
│   └── Transaction History
│
└── Flask Web Dashboard
    ├── 💳 Payment Records Table
    ├── ➕ Add New Payments
    ├── 🗑️  Delete Transactions
    ├── 📥 Download Reports
    └── 📊 Payment Statistics
```
---
## 📸 Dashboard Preview


- 📷 **Reports Section**  
  ![Reports Section](AWS-S3-LAMBDA-RDS-PAGOSWEBSITE/reportedepagos.png)

- 📷 **Add Payment Form**  
  ![Add Payment Form](AWS-S3-LAMBDA-RDS-PAGOSWEBSITE/agregarnuevospagos.png)

- 📷 **Main Payment Dashboard**  
  ![Main Payment Dashboard](AWS-S3-LAMBDA-RDS-PAGOSWEBSITE/tabladepagos.png)

---

## 🛠️ Tech Stack

<div align="center">

![AWS](https://img.shields.io/badge/AWS-FF9900?style=flat-square&logo=amazon-aws&logoColor=white)
![Python](https://img.shields.io/badge/Python%203.11-3776AB?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34C26?style=flat-square&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![Boto3](https://img.shields.io/badge/Boto3-FF9900?style=flat-square&logo=amazon-aws&logoColor=white)

</div>

---

## 📋 Project Overview

This project demonstrates enterprise-level serverless architecture combining AWS cloud services with a modern web dashboard. It provides an end-to-end solution for automated payment processing, reporting, and management.

**Core Capabilities:**
- 💚 Automatic daily report generation via AWS Lambda at scheduled times
- 📊 Real-time payment data visualization and management
- ☁️ Cloud-native, zero-infrastructure-management architecture
- 🔄 Complete CRUD (Create, Read, Update, Delete) payment operations
- 💾 Seamless S3 integration for report archival and distribution
- 🔐 Enterprise-grade security with IAM access control

---

## 🔗 AWS Components

### 🗄️ **Amazon RDS - MySQL Database**
Reliable relational database for payment data persistence:
- 👤 **Customer Information** — First name, last name
- 🆔 **Unique Identification** — ID number (Cedula)
- 💰 **Payment Records** — Transaction amounts
- 📅 **Timestamp Data** — Payment dates and times
- 🔍 **Query Capability** — Full SQL support for complex reporting

### ⚡ **AWS Lambda - Serverless Compute**
Autonomous report generation function:
- ⏰ **Scheduled Triggers** — Executes daily at 8:00 AM via EventBridge
- 📊 **Data Query** — Retrieves previous day's payment transactions
- 📄 **PDF Generation** — Creates professional payment summary reports
- 📈 **Statistics** — Calculates totals and transaction counts
- 📤 **S3 Upload** — Automatically distributes reports to S3 bucket
- 🚨 **Error Handling** — Comprehensive logging and failure notifications

### 💾 **Amazon S3 - Object Storage**
Scalable cloud storage for report archival:
- 📚 **Report Storage** — Long-term retention of all generated PDFs
- 🔗 **Easy Retrieval** — Organized folder structure by date
- 🔐 **Security** — Encryption at rest and in transit
- 🌍 **Accessibility** — Pre-signed URLs for secure external access
- 💪 **Durability** — 99.999999999% data durability guarantee

### 🌐 **Flask Web Application**
Modern, responsive user interface:
- 📋 **Payment Dashboard** — Real-time table with all transactions
- ➕ **Add Payments** — Form to insert new payment records
- 🗑️ **Delete Records** — Remove payment entries by ID
- 📥 **Report Downloads** — Access archived reports from S3
- 📱 **Responsive Design** — Optimized for desktop and mobile devices

---

## 🚀 Quick Start

```bash
# 1. Clone the repository
git clone (https://github.com/ANDFS2411x/AWS-S3-LAMBDA-RDS-PAGOS-WEBSITE/)
cd AWS-S3-LAMBDA-RDS-PAGOS-WEBSITE

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure your AWS credentials
# Set up your AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY

# 4. Update database configuration
# Edit DB_CONFIG in app.py with your RDS endpoint

# 5. Run the Flask application
python app.py

# 6. Open browser and navigate to http://localhost:5000
```

---

## 📁 Project Structure

```
AWS-S3-LAMBDA-RDS-PAGOS-WEBSITE/
├── README.md
└── AWS-S3-LAMBDA-RDS-PAGOSWEBSITE/
    ├── app.py                 # Flask application
    ├── templates/
    │   ├── formulario.html    # Payment form
    │   ├── tabla.html         # Payment records table
    │   └── reportes.html      # Reports section
    └── static/                # CSS, JavaScript files
```

---

## 🔧 Configuration

### Environment Variables
```env
DB_HOST=your-rds-endpoint.rds.amazonaws.com
DB_USER=admin
DB_PASSWORD=your-secure-password
DB_NAME=payment_database
S3_BUCKET=your-bucket-name
AWS_REGION=us-east-1
```

### Database Schema
```sql
CREATE TABLE pagos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(100) NOT NULL,
    Apellido VARCHAR(100) NOT NULL,
    Cedula VARCHAR(20) UNIQUE NOT NULL,
    Valor_PagosPagado DECIMAL(10, 2) NOT NULL,
    Fecha_Consignacion DATE NOT NULL
);
```

---

## 🎯 Usage Workflow

1. **View Payments** — Navigate to the home page to see all payment records
2. **Add Payment** — Click "Agregar Pago" to add a new payment record
3. **Download Reports** — Access pre-generated reports from the Reports section
4. **Automated Reports** — Lambda automatically generates reports daily at 8:00 AM
5. **Archive** — Reports are automatically saved to S3 for long-term storage

---

<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Poppins&size=16&duration=3000&pause=1000&color=10B981&center=true&vCenter=true&width=500&lines=Built+with+AWS+%26+Python;Serverless+%26+Scalable" alt="Built with" />



## 👨‍💻 Author

**Andrés Fábregas**  
Software Developer & Cloud Architect

---

<div align="center">

⭐ If you found this project helpful, please consider giving it a star! ⭐

</div>
