## Dataset Used: Online Retail Dataset

This project uses the **Online Retail Dataset**, a real-world transactional dataset containing sales records of an online retail store. The dataset includes transactions that occurred between **2010 and 2011**, capturing purchases made by customers from multiple countries.

### Dataset Features

The dataset contains the following important fields:

| Column      | Description                            |
| ----------- | -------------------------------------- |
| InvoiceNo   | Unique identifier for each transaction |
| StockCode   | Unique product/item code               |
| Description | Product name                           |
| Quantity    | Number of items purchased              |
| InvoiceDate | Date and time of transaction           |
| UnitPrice   | Price per unit of product              |
| CustomerID  | Unique customer identifier             |
| Country     | Country where the customer is located  |

This dataset represents a **typical retail transaction system**, making it ideal for building and demonstrating data engineering pipelines.

---

## Why This Dataset Was Chosen

The Online Retail dataset was selected for the following reasons:

### 1️⃣ Real-world transactional data

The dataset contains real sales transactions, making it suitable for simulating **industry-level data processing pipelines**.

### 2️⃣ Ideal for ETL pipelines

The dataset contains raw, uncleaned data with:

* Missing values
* Negative quantities (returns)
* Multiple date formats

This makes it perfect for demonstrating **data cleaning and transformation in an ETL pipeline**.

### 3️⃣ Supports business analytics

The dataset allows useful analytics such as:

* Revenue analysis
* Sales by country
* Monthly sales trends
* Product performance

### 4️⃣ Suitable size for Big Data tools

The dataset is large enough to demonstrate distributed data processing using **Apache Spark**, while still being manageable for development and experimentation.

### 5️⃣ Industry-relevant structure

Retail datasets like this are commonly used in:

* E-commerce analytics
* Customer behavior analysis
* Sales forecasting
* Business intelligence dashboards

---

## Use Case in This Project

In this project, the dataset is used to build an **ETL pipeline using Apache Spark**, where:

1. Raw CSV data is ingested
2. Data cleaning and preprocessing are performed
3. New features such as **Revenue** are created
4. Business analytics are generated
5. Processed data is stored in **Parquet format for efficient querying**

This demonstrates a typical **data engineering workflow used in real-world analytics systems**.
