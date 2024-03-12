-- Schema for Redshift

CREATE TABLE records (
    passengerid BIGINT,
    survived BIGINT,
    pclass BIGINT,
    name VARCHAR(255),
    sex VARCHAR(10),
    age DOUBLE PRECISION,
    sibsp BIGINT,
    parch BIGINT,
    ticket VARCHAR(255),
    fare DOUBLE PRECISION,
    cabin VARCHAR(255),
    embarked VARCHAR(10)
    
);
-- To Query the data after running ETL job
SELECT
    *
FROM
    "dev"."public"."records";
