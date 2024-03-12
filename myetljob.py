import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue import DynamicFrame

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node Amazon S3
AmazonS3_node1710225665423 = glueContext.create_dynamic_frame.from_catalog(
    database="database",
    table_name="aws_glue_etl_proj",
    transformation_ctx="AmazonS3_node1710225665423",
)

# Script generated for node Amazon Redshift
AmazonRedshift_node1710225667262 = glueContext.write_dynamic_frame.from_options(
    frame=AmazonS3_node1710225665423,
    connection_type="redshift",
    connection_options={
        "redshiftTmpDir": "s3://aws-glue-assets-767397934638-us-east-1/temporary/",
        "useConnectionProperties": "true",
        "dbtable": "public.records",
        "connectionName": "Redshift connection",
        "preactions": "CREATE TABLE IF NOT EXISTS public.records (passengerid BIGINT, survived BIGINT, pclass BIGINT, name VARCHAR, sex VARCHAR, age DOUBLE PRECISION, sibsp BIGINT, parch BIGINT, ticket VARCHAR, fare DOUBLE PRECISION, cabin VARCHAR, embarked VARCHAR);",
    },
    transformation_ctx="AmazonRedshift_node1710225667262",
)

job.commit()
