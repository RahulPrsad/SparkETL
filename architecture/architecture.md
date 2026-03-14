## ETL Pipeline Architecture

The ETL (Extract, Transform, Load) pipeline for the **Online Real Estate Dataset** follows a structured workflow from raw data ingestion to clean, analyzable data storage. Below is a detailed description of each step:

### 1️⃣ Ingestion
- **Raw E-Commerce CSV Dataset:** The pipeline starts with the raw CSV dataset containing all property or transaction records.
- **Create Spark Session using PySpark:** Initializes a Spark session to handle large-scale distributed data processing.
- **Read CSV Data using `spark.read.csv()`:** Reads the raw dataset into a Spark DataFrame for further processing.

### 2️⃣ Data Cleaning
- **Remove Null Values:** Cleans the dataset by removing rows with missing critical information.
- **Fix Data Types:** Ensures columns have correct types (e.g., numeric, date) for accurate transformations.
- **Remove Duplicate Records:** Eliminates duplicate entries to maintain data quality and integrity.

### 3️⃣ Transformation
- **Create Feature `total_sales = price * quantity`:** Derives new columns to enrich the dataset for analytics.
- **Standardize Columns:** Ensures column names and formats are consistent across the dataset.
- **Filter Invalid Records:** Removes any data entries that are out of expected ranges or have invalid values.

### 4️⃣ Aggregation
- **Sales per Category:** Aggregates data by property type, category, or other dimensions.
- **Daily or Monthly Sales:** Aggregates sales over time for trend analysis and reporting.

### 5️⃣ Storage
- **Load Clean Data into Parquet Format:** Instead of MySQL, the cleaned and transformed data is stored as a **Parquet file** on Databricks (`/Volumes/workspace/stream/streaming/clean_retail_data`).
- **Data Available for Analysis and Reporting:** The Parquet file can be directly used for analytics, dashboards, or further Spark processing.

---

💡 **Why Parquet:**  
- Columnar storage → faster queries for analytics.  
- Efficient compression → smaller storage size.  
- Fully compatible with Spark → ideal for ETL pipelines and dashboards.  
- Cloud-friendly → no external database setup needed.
