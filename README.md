# ETL Project with AWS Glue: Moving Data from S3 to Redshift.

### Overview
This project implements an Extract, Transform, Load (ETL) process to move data from Amazon S3 to Amazon Redshift using AWS Glue services. The architecture comprises several components including S3 buckets, AWS Glue Crawlers, Glue Data Catalog, Glue Jobs, and Amazon Redshift.

### Architecture
The architecture of the ETL process is as follows:

**Amazon S3:** Source data files are stored in Amazon S3 buckets. These files may be in various formats such as CSV, JSON, or Parquet.

**AWS Glue Crawler:** A Glue Crawler is used to automatically discover and catalog metadata about the source data files stored in S3. It scans the data and creates or updates tables in the Glue Data Catalog based on the schema inferred from the data.

**Glue Data Catalog:** The Glue Data Catalog serves as the central metadata repository for the ETL process. It contains information about the source data files and the target tables in Amazon Redshift.

**AWS Glue Jobs:** Glue Jobs are used to perform the ETL operations. These jobs extract data from the source tables in the Glue Data Catalog, apply transformation logic, and load the transformed data into target tables in Amazon Redshift.

**Amazon Redshift:** Amazon Redshift is used as the data warehouse where the transformed data is loaded. It provides scalable, high-performance storage and query processing capabilities for analytics and reporting.

### Setup
#### Prerequisites
- An AWS account with permissions to create and manage Glue resources, S3 buckets, Amazon Redshift clusters, and IAM roles.
- Data files stored in Amazon S3 buckets.
- An Amazon Redshift cluster configured with the appropriate schema and permissions.
### IAM Setup
#### Create IAM Roles:
- Create an IAM role for Glue service with permissions to access S3 buckets and Redshift clusters.
- Attach policies like AmazonS3ReadOnlyAccess and AmazonRedshiftFullAccess to the IAM role.
#### Attach IAM Roles:

- Attach the IAM role created for Glue service to the AWS Glue Crawlers and Glue Jobs for access to S3 and Redshift resources.
### Configuration

**AWS Glue Crawler:**
- Create a Glue Crawler to crawl the S3 buckets and catalog the metadata.
- Specify the S3 paths to crawl and the target database in the Glue Data Catalog.
  
**Glue Data Catalog:**
- Verify that the Glue Crawler has created or updated the necessary tables in the Glue Data Catalog.

**AWS Glue Jobs:**
- Create Glue Jobs to perform the ETL operations.
- Specify the source and target tables in the Glue Data Catalog, along with the transformation logic.

**Amazon Redshift:**
- Ensure that the Redshift cluster is running and accessible.
- Create the target tables in Redshift with the appropriate schema to match the transformed data.
### Execution

#### Run Glue Jobs:
- Run the Glue Jobs to extract, transform, and load the data from S3 to Redshift.
### Monitoring and Maintenance
- Monitor the execution of Glue Jobs for errors or performance issues.
- Regularly review and update the Glue Crawler configuration to ensure accurate metadata cataloging.
- Monitor the health and performance of the Amazon Redshift cluster for optimal query processing
