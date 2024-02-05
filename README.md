# Stack-Overflow-Data-Pipeline
An end-to-end ETL pipeline implemented on Azure ecosystem to collect, process a large dataset of Stack Overflow posts to identify the trending topics per day and users' geolocation and statistics information per country, and provide visual insights using Tableau dashboards.

## Overview
The primary goal of this pipeline is to understand the daily trending topics on Stack Overflow community and users' statistics information (geolocation distribution and reputation). 
The end to end pipeline is implemented using Azure services (Azure Data Factory, Azure DataBricks, Azure Blob Storage, Azure SQL Database, Azure Function) to process several files of input using Spark clusters, have the results stored in Azure Data Lake and copy them to Azure SQL Tables. The project leverages Tableau BI Tool to connect to the SQL Tables and create a dashboard for analytics and reporting purpose.

## System Architecture Overview
![WeCloudDataProjects-Phase2_BigDataEngineering](https://github.com/khojashaheen/Stack-Overflow-Data-Pipeline/assets/132402838/b7f71c93-6b3d-4e72-822d-aa855b354538)


## Installation


## Pre-requisites
