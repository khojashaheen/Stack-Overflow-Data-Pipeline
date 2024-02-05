# Create Data Factory Pipelines

## Step 0. Pre-requisite:
#### 0.1 run script 'Azure_SQL_DDL.sql' to create SQL Tables
#### 0.2 create Azure Function, and deploy the code in 'Azure_function_get_world_population.py'
#### 0.3 create spark clusters on databricks and deploy databricks notebooks found under 'Scripts' folder in the following order:
	- Mount Storage Container.ipynb
	- Project_Model_Training_RF.ipynb
	- Project_Model_Deployment_RF.ipynb
	- User's Geolocation.ipynb


## Step 1. Create 6 Linked Service
#### 1.1 create RDS Linked Service to link the RDS postgres database and provide connection details (host, username, password, database, port)
#### 1.2 create blob storage Linked Service to link the public external Storage Blob and provide storage account details
#### 1.3 create azure function Linked Service to perform the web scraping logic and read from a Wikipedia table
#### 1.4 create blob storage Linked Service to link to our own data lake and provide storage account details
#### 1.5 create azure databricks Linked Service to invoke notebooks for data transformation
#### 1.6 create azure SQL Linked Service to link to the Azure SQL service

## Step 2. Create Datasets
#### 2.1 create datasets for Source:
	- rds_users: represent Users Table on postgres
	- rds_postTypes: represent PostTypes Table on postgres
	- blob_posts_wcd: represent parquet files on WeCloudData's storage blob
	- blob_geolocation_input: represent json file on storage blob

#### 2.2 create datasets for Intermediary transformation:
	- blob_users: represent users data stored on Data Lake
	- blob_posttypes: represent posttypes data stored on Data Lake
	- blob_posts: represent posts data stored on Data Lake
	- blob_ml_results: represent csv results from ML model that classifies posts' topics on Data Lake
	- blob_geo_location_csv: represent csv results from PySpark Notebook related to countries' statistics on Data Lake 
	- blob_users_output: represent the csv results from PySpark Notebook related to top users per country

#### 2.3 create datasets for SQL Tables:
	- sql_countries_table: represent 'countries' Table on Azure SQL
	- sql_top_users_table: represent 'countries_top_users' Table on Azure SQL
	- sql_topics_table: represent 'topics' Table on Azure SQL


## Step 3. Create Pipeline

#### 3.1 copy and process posts data every day

#### 3.2 copy and process users and post types data every week

#### 3.3 retrieve world population once a year


