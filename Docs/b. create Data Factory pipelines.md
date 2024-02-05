# Create Data Factory Pipelines

## Step 0. Pre-requisite:
	- run script 'Azure_SQL_DDL.sql' to create SQL Tables
	- create Azure Function, and deploy the code in 'Azure_function_get_world_population.py'
	- create spark clusters on databricks and deploy databricks notebooks found under 'Scripts' folder in the following order:
		- Mount Storage Container.ipynb
		- Project_Model_Training_RF.ipynb
		- Project_Model_Deployment_RF.ipynb
		- User's Geolocation.ipynb


## Step 1. Create Linked Service
	- create RDS Linked Service to link the RDS postgres database and provide connection details (host, username, password, database, port)
	- create blob storage Linked Service to link the public external Storage Blob and provide storage account details
	- create azure function Linked Service to perform the web scraping logic and read from a Wikipedia table
	- create blob storage Linked Service to link to our own data lake and provide storage account details
	- create azure databricks Linked Service to invoke notebooks for data transformation
	- create azure SQL Linked Service to link to the Azure SQL service

## Step 2. Create Datasets
#### 2.1 create datasets for Source:
	- rds_users: represent Users Table on postgres
	- rds_postTypes: represent PostTypes Table on postgres
	- blob_posts_wcd: represent parquet files on WeCloudData's storage blob
	- blob_geolocation_input: represent json file on storage blob

#### 2.2 create datasets for intermediary transformation:
	- blob_users: represent users data stored on Data Lake
	- blob_posttypes: represent posttypes data stored on Data Lake
	- blob_posts: represent posts data stored on Data Lake
	- blob_ml_results: represent csv results from ML model that classifies posts' topics on Data Lake
	- blob_geo_location_csv: represent csv results from PySpark Notebook related to countries' statistics on Data Lake 
	- blob_users_output: represent the csv results from PySpark Notebook related to top users per country

#### 2.3 create datasets for SQL tables:
	- sql_countries_table: represent 'countries' Table on Azure SQL
	- sql_top_users_table: represent 'countries_top_users' Table on Azure SQL
	- sql_topics_table: represent 'topics' Table on Azure SQL



## Step 3. Create Pipeline

#### 3.1 copy and process posts data every day
<img width="800" alt="Pipeline1" src="https://github.com/khojashaheen/Stack-Overflow-Data-Pipeline/assets/132402838/c2907265-06e4-43e2-a8dd-7ba7ca10d65e">


#### 3.2 copy and process users and post types data every week
<img width="800" alt="Pipeline2" src="https://github.com/khojashaheen/Stack-Overflow-Data-Pipeline/assets/132402838/143d3fc4-e033-426c-a71b-42417399815f">


#### 3.3 retrieve world population once a year
<img width="800" alt="Pipeline3" src="https://github.com/khojashaheen/Stack-Overflow-Data-Pipeline/assets/132402838/96484372-b3c6-4052-8cc4-9ecbc13af86b">



