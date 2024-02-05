# Stack-Overflow-Data-Pipeline
An end-to-end ETL pipeline implemented on Azure ecosystem to collect, process a large dataset of Stack Overflow posts to identify the trending topics per day and users' geolocation and statistics information per country, and provide visual insights using Tableau dashboards.

## Overview
The primary goal of this pipeline is to understand the daily trending topics on Stack Overflow community and users' statistics information (geolocation distribution and reputation per cuntry). 

<img width="320" alt="Dashboard_Topic" src="https://github.com/khojashaheen/Stack-Overflow-Data-Pipeline/assets/132402838/a45381c1-7159-42e3-af29-cbfbd2aaec3e">
<img width="328" alt="Dashboard_Users" src="https://github.com/khojashaheen/Stack-Overflow-Data-Pipeline/assets/132402838/169ec000-7f4e-4aa4-9035-5f981e820c93">
<img width="320" alt="Dashboard_Users_Per_Country" src="https://github.com/khojashaheen/Stack-Overflow-Data-Pipeline/assets/132402838/58d1e06b-fb4d-4ca4-bfcc-0f973aa9fbb6">


## System Architecture Overview
The end to end pipeline is implemented using Azure services (Azure Data Factory, Azure DataBricks, Azure Blob Storage, Azure SQL Database, Azure Function) to store several files of input from various sources to the Azure Data Lake, process these files using Spark clusters, have the results stored in Azure Data Lake and copy them to Azure SQL Tables. The project leverages Tableau BI Tool to connect to the SQL Tables and create a dashboard for analytics and reporting purpose.

![WeCloudDataProjects-Phase2_BigDataEngineering](https://github.com/khojashaheen/Stack-Overflow-Data-Pipeline/assets/132402838/b7f71c93-6b3d-4e72-822d-aa855b354538)


## Pre-requisites
  - Azure Account
  - Tableau Account

## Installation
#### Step 1. Clone the Repository:
  - Use git clone https://github.com/khojashaheen/Stack-Overflow-Data-Pipeline to clone this repository to your local machine.
  
#### Step 2. Complete Pre-requisites Steps
#### Step 3. Create Azure Virtual machine, Storage Account, Container and Folder following the guideline [Azure VM and Storage Setup Doc](Docs/a.Create%20Azure%20VM%20and%20Storage%20Account.md)
#### Step 4. Create Azure Data Factory Pipelines following the guideline [Data Factory Pipeline Creation Doc](Docs/b.%20create%20Data%20Factory%20pipelines.md)
#### Step 5: Validate data flow from source (RDS,Blob Storage,Azure Function) to Destination (Azure SQL)
#### Step 6: Login to Tableau BI tool, connect to Azure SQL databases and import [Tableau Workbook Dashboard](Tableau/Phase%202%20Dashboard.twbx)



