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

**A powerful serverless payment management system combining AWS Cloud Services with a modern, interactive web dashboard for real-time payment tracking and automated report generation.**

?? *Automated � Scalable � Serverless � Real-time* 

</div>

---

## ? Key Features

?? **Fully Automated Reports** � Scheduled daily payment generation at 8:00 AM using EventBridge  
?? **Real-time Web Dashboard** � Interactive Flask interface for live payment tracking  
?? **AWS Lambda Processing** � Serverless PDF report generation with zero infrastructure overhead  
??? **MySQL RDS Storage** � Secure relational database with comprehensive payment records  
?? **S3 Cloud Storage** � Automatic report archival with pre-signed secure downloads  
?? **Complete CRUD Operations** � Add, view, update, and delete payment transactions  
?? **Enterprise Security** � IAM roles, least privilege access, and secure credential management  
?? **Responsive UI** � Beautiful, modern web interface accessible on all devices  

---

## ??? System Architecture

This project integrates multiple AWS services into a cohesive, serverless payment management ecosystem:

```
+--------------------------------------------------------------+
�           AWS AUTOMATED PAYMENT REPORTING SYSTEM             �
+--------------------------------------------------------------�
�                                                              �
�  EVENT-DRIVEN AUTOMATION                                     �
�  +--------------+    +--------------+    +----------+       �
�  � EventBridge  �---?�   Lambda     �---?�   S3     �       �
�  �  Daily       �    �  PDF Report  �    �  Archive �       �
�  �  8:00 AM     �    �  Generation  �    �  Storage �       �
�  +--------------+    +--------------+    +----------+       �
�         �                    �                               �
�         +----------------------------------+                �
�                                            �                �
�                                   +--------?---------+      �
�                                   �   RDS MySQL      �      �
�                                   �  Payment DB      �      �
�                                   �  � Names         �      �
�                                   �  � IDs           �      �
�                                   �  � Amounts       �      �
�                                   �  � Dates         �      �
�                                   +------------------+      �
�                                            ?                �
�                                            �                �
�  USER INTERFACE LAYER                      �                �
�  +------------------------------------------------------+   �
�  �         Flask Web Dashboard                         �   �
�  �  +------------------------------------------------+ �   �
�  �  � ?? Payment Records Table                       � �   �
�  �  � ? Add New Payments                           � �   �
�  �  � ???  Delete Transactions                       � �   �
�  �  � ?? Download Reports (S3 Integration)          � �   �
�  �  � ?? View Payment Statistics                    � �   �
�  �  +------------------------------------------------+ �   �
�  +-----------------------------------------------------+   �
�                                                              �
+--------------------------------------------------------------+
```

---

## ?? Tech Stack

<div align="center">

![AWS](https://img.shields.io/badge/AWS-FF9900?style=flat-square&logo=amazon-aws&logoColor=white)
![Python](https://img.shields.io/badge/Python%203.11-3776AB?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34C26?style=flat-square&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![PyMySQL](https://img.shields.io/badge/PyMySQL-4479A1?style=flat-square&logo=python&logoColor=white)
![Boto3](https://img.shields.io/badge/Boto3-FF9900?style=flat-square&logo=amazon-aws&logoColor=white)
![JSON](https://img.shields.io/badge/JSON-000000?style=flat-square&logo=json&logoColor=white)

</div>

---

## ?? Project Overview

This project demonstrates enterprise-level serverless architecture combining AWS cloud services with a modern web dashboard. It provides an end-to-end solution for automated payment processing, reporting, and management.

**Core Capabilities:**
- ? Automatic daily report generation via AWS Lambda at scheduled times
- ?? Real-time payment data visualization and management
- ?? Cloud-native, zero-infrastructure-management architecture
- ?? Complete CRUD (Create, Read, Update, Delete) payment operations
- ?? Seamless S3 integration for report archival and distribution
- ?? Enterprise-grade security with IAM access control

---

## ?? Core AWS Components

### ?? **Amazon RDS - MySQL Database**
Reliable relational database for payment data persistence:
- ?? **Customer Information** � First name, last name
- ?? **Unique Identification** � ID number (Cedula)
- ?? **Payment Records** � Transaction amounts
- ?? **Timestamp Data** � Payment dates and times
- ?? **Query Capability** � Full SQL support for complex reporting

### ?? **AWS Lambda - Serverless Compute**
Autonomous report generation function:
- ? **Scheduled Triggers** � Executes daily at 8:00 AM via EventBridge
- ?? **Data Query** � Retrieves previous day's payment transactions
- ?? **PDF Generation** � Creates professional payment summary reports
- ?? **Statistics** � Calculates totals and transaction counts
- ?? **S3 Upload** � Automatically distributes reports to S3 bucket
- ?? **Error Handling** � Comprehensive logging and failure notifications

### ?? **Amazon S3 - Object Storage**
Scalable cloud storage for report archival:
- ?? **Report Storage** � Long-term retention of all generated PDFs
- ?? **Easy Retrieval** � Organized folder structure by date
- ?? **Pre-signed URLs** � Secure temporary download links
- ?? **Access Control** � IAM policies for restricted access
- ?? **Versioning** � Track report history and changes
- ?? **Cost Efficient** � Pay only for storage used

### ?? **Amazon EventBridge - Event Scheduling**
Precision timing for automated workflows:
- ?? **Cron Expression** � `0 8 * * ? *` (8:00 AM daily)
- ?? **Lambda Trigger** � Direct integration with Lambda functions
- ?? **Event Logging** � Complete audit trail of executions
- ? **Zero Overhead** � Serverless event routing, no infrastructure

### ??? **AWS IAM - Identity & Access Management**
Enterprise security with least privilege principle:
- ?? **User Roles** � Separate accounts for Lambda and database access
- ?? **Access Keys** � Secure credential management
- ?? **Permissions** � Granular policy restrictions per service
- ?? **Audit Trail** � Complete logging of all API calls

---

## ?? Web Dashboard - Flask Application

### Dashboard Features

**?? Payment Records Display**
- Tabular view of all payment transactions
- Sortable columns for easy data browsing
- Clean, intuitive interface design

**? Add New Payments**
- Form-based payment entry
- Input validation and error handling
- Real-time database updates

**??? Delete Transactions**
- Quick deletion by ID
- Confirmation prompts for safety
- Immediate UI refresh after deletion

**?? S3 Report Downloads**
- Direct integration with S3 storage
- Pre-signed secure URLs
- Download report history

**?? Responsive Design**
- Mobile-friendly interface
- Cross-browser compatibility
- Modern CSS styling

---

## ?? Project Structure

```
AWS-S3-LAMBDA-RDS-PAGOS-WEBSITE/
�
+-- README.md                          # Project documentation
�
+-- AWS-S3-LAMBDA-RDS-PAGOSWEBSITE/   # Main application directory
�   +-- app.py                         # Flask application & routes
�   �   +-- Database connections
�   �   +-- Payment CRUD operations
�   �   +-- S3 integration
�   �
�   +-- templates/                     # HTML templates
�       +-- tabla.html                 # Payment records display
�       +-- formulario.html            # Payment entry form
�       +-- reportes.html              # Report management page
```

---

## ?? Quick Start Guide

### Prerequisites
- ?? **AWS Account** with appropriate permissions
- ?? **Python 3.11+** installed locally
- ?? **pip** package manager
- ?? **Git** for version control

### Installation Steps

**1?? Clone the Repository**
```bash
git clone https://github.com/yourusername/AWS-S3-LAMBDA-RDS-PAGOS-WEBSITE.git
cd AWS-S3-LAMBDA-RDS-PAGOS-WEBSITE
```

**2?? Install Python Dependencies**
```bash
pip install -r requirements.txt
```

**3?? Configure AWS Credentials**
```bash
aws configure
```

**4?? Start the Flask Application**
```bash
cd AWS-S3-LAMBDA-RDS-PAGOSWEBSITE
python app.py
```

Application will be available at: `http://localhost:5000`

---

## ?? Security Best Practices

? **Least Privilege Access** � IAM users have minimal required permissions  
? **Environment Variables** � Sensitive data stored securely  
? **S3 Pre-signed URLs** � Secure temporary access links  
? **Database Encryption** � RDS encryption at rest and in transit  
? **API Security** � CORS configuration and input validation  
? **Audit Logging** � CloudTrail logging for all AWS API calls  
? **Public Access Block** � S3 bucket configured with public access denied  

---

<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Poppins&size=18&duration=3000&pause=1000&color=10B981&center=true&vCenter=true&width=600&lines=Built+with+%E2%98%81%EF%B8%8F+and+AWS;Enterprise+Payment+Solutions" alt="Built with AWS"/>

<br/>

### ?? **Author**

Made with ?? by **Andr�s F�bregas** (ANDFS2411x)  
*Full-Stack Developer | Cloud Solutions Architect*

<br/>

</div>

---

**Last Updated:** January 2026 | **Version:** 1.0.0 | **Status:** ? Production Ready
