## Car Sales Report Analysis Using SQL.

This project is based on Car Sales Report data set downloaded from kaggle.
Dataset Link- https://www.kaggle.com/datasets/missionjee/car-sales-report

# Car Sales Analytics (PostgreSQL, SQL Window Functions)

A compact analytics project demonstrating **data modeling**, **SQL analytics**, **customer segmentation**, **pricing insights**, and **business storytelling** using a car sales dataset. Built to showcase **entry-level data scientist** capabilities with practical, resume-ready outcomes.

> **Tech Stack:** PostgreSQL (primary), SQL (CTEs & window functions)  
> **Optional (for notebook demos):** Google Colab + SQLite, pandas, matplotlib

---

## 🎯 Objectives

- Model a clean car sales schema in PostgreSQL.
- Answer high-impact business questions with **CTEs, window functions, and statistical summaries**.
- Deliver actionable insights: trends, dealer/region performance, product mix, pricing premiums, and customer segmentation.
- Package results for **portfolio/recruiter review** and **repeatable execution**.

---

## 🗃️ Dataset & Schema

**Table:** `car_sales`

```sql
car_id        VARCHAR(20) PRIMARY KEY NOT NULL,
dates         DATE,
customer_name CHAR(20),
gender        CHAR(10),
annual_income INT,
dealer_name   VARCHAR(80),
company       VARCHAR(40),
model         VARCHAR(30),
engine        VARCHAR(60),
transmission  VARCHAR(30),
color         VARCHAR(10),
price         INT,
dealer_no     VARCHAR(12),
body_style    VARCHAR(20),
phone         INT,
dealer_region VARCHAR(30)
