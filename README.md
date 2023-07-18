# Data Pipeline Automation With Airflow

## Project Description
This project focuses on automating and monitoring the ETL (Extract, Transform, Load) pipelines of Sparkify, a music streaming company. The pipelines are implemented using Apache Airflow, which provides a scalable and reliable platform for orchestrating data workflows. By introducing automation and monitoring, Sparkify aims to improve the efficiency and quality of their data processes.

The project involves building high-grade data pipelines that are dynamic and built from reusable tasks. These pipelines extract JSON logs and metadata from Amazon S3 and load the transformed data into Sparkify's data warehouse on Amazon Redshift. Data quality checks are incorporated to ensure the accuracy and integrity of the data.

## Project Structure
The project directory is organized as follows:

- `dags/`: This directory contains the DAG (Directed Acyclic Graph) definition file(s) for Apache Airflow. The main DAG file, `final_project.py`, orchestrates the workflow and defines the sequence of tasks.
- `plugins/operators/`: This directory contains custom operators used in the DAGs. The operators handle specific tasks such as staging data from S3 to Redshift, loading dimension and fact tables, and performing data quality checks.
- `plugins/helpers/`: This directory contains helper functions and SQL queries used by the operators.

## Prerequisites
Before running the project, ensure the following prerequisites are met:

- Apache Airflow is installed and properly configured.
- Amazon Redshift is set up with the required tables.
- AWS credentials are properly configured to access S3 and Redshift.

## DAG Structure
The main DAG, `final_project.py`, consists of the following tasks:

1. Staging the data: The JSON logs and metadata files are staged from S3 to Redshift staging tables using the `StageToRedshiftOperator`.
2. Loading the fact table: The fact table (`songplays`) is loaded with data from the staging tables using the `LoadFactOperator`.
3. Loading the dimension tables: The dimension tables (`users`, `songs`, `artists`, and `time`) are loaded with data from the staging tables using the `LoadDimensionOperator`.
4. Data quality checks: Data quality checks are performed using the `DataQualityOperator` to ensure the validity of the loaded data.

## Usage
1. Set up Apache Airflow and create a new DAG.
2. Copy the contents of the `dags/final_project.py` file into your DAG file.
3. Copy the operator files from the `plugins/operators/` directory to your project's `plugins/operators/` directory.
4. Copy the helper files (`plugins/helpers/sql_queries.py`) to your project's `plugins/helpers/` directory.
5. Execute the DAG in Apache Airflow to start the data pipeline.
