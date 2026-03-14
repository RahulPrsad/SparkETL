# Generated from: Spark_ETL_Pipeline.ipynb
# Converted at: 2026-03-14T20:24:27.059Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

df = spark.read.format("csv") \
.option("header","true") \
.option("inferSchema","true") \
.load("/Volumes/workspace/stream/streaming/Online Retail.csv")

display(df)


"""Why

To understand:

column names

data types

structure of dataset"""
df.printSchema()


df = df.dropna()

display(df)


df = df.filter(df.Quantity > 0)

display(df)


from pyspark.sql.functions import trim

df = df.withColumn("InvoiceDate", trim("InvoiceDate"))


from pyspark.sql.functions import to_timestamp, coalesce

df = df.withColumn(
    "InvoiceDate",
    coalesce(
        to_timestamp("InvoiceDate", "MM/dd/yyyy HH:mm:ss"),
        to_timestamp("InvoiceDate", "dd/MM/yyyy HH:mm:ss")
    )
)

display(df)
df.printSchema()


from pyspark.sql.functions import col

df = df.withColumn("Revenue", col("Quantity") * col("UnitPrice"))
df.select("Quantity","UnitPrice","Revenue").show(10)





from pyspark.sql.functions import sum

sales_by_country = df.groupBy("Country") \
.agg(sum("Revenue").alias("TotalRevenue")) \
.orderBy("TotalRevenue", ascending=False)

display(sales_by_country)


from pyspark.sql.functions import month

df = df.withColumn("Month", month("InvoiceDate"))

display(df.select("InvoiceDate", "Month"))

from pyspark.sql.functions import sum

monthly_sales = df.groupBy("Month") \
    .agg(sum("Revenue").alias("MonthlyRevenue")) \
    .orderBy("Month")

display(monthly_sales)


top_products = df.groupBy("Description") \
.agg(sum("Quantity").alias("TotalSold")) \
.orderBy("TotalSold", ascending=False)

display(top_products)


df_clean.write \
.mode("overwrite") \
.parquet("/Volumes/workspace/stream/streaming/clean_retail_data")

df_saved = spark.read.parquet("/Volumes/workspace/stream/streaming/clean_retail_data")

display(df_saved)



df.write \
.mode("overwrite") \
.partitionBy("Month") \
.parquet("/Volumes/workspace/stream/streaming/clean_retail_data")


df_saved = spark.read.parquet("/Volumes/workspace/stream/streaming/clean_retail_data")
display(df_saved)