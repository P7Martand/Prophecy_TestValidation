{{
  config({    
    "materialized": "ephemeral",
    "database": "qa_team",
    "schema": "qa_database"
  })
}}

WITH ALL_TYPE_TABLE_2 AS (

  SELECT *
  
  FROM {{ prophecy_tmp_source('parent_pipeline', 'ALL_TYPE_TABLE_2') }}

),

Reformat_3 AS (

  SELECT 
    C_NUM AS C_NUM,
    C_NUM10 AS C_NUM10,
    C_DEC AS C_DEC,
    C_NUMERIC AS C_NUMERIC,
    C_INT AS C_INT,
    C_INTEGER AS C_INTEGER,
    C_DOUBLE AS C_DOUBLE,
    C_FLOAT AS C_FLOAT,
    C_COUBLE_PRECISION AS C_COUBLE_PRECISION,
    C_REAL AS C_REAL,
    C_VARCHAR AS C_VARCHAR,
    C_BOOL AS C_BOOL,
    C_TIMESTAMP AS C_TIMESTAMP,
    C_DATE AS C_DATE
  
  FROM ALL_TYPE_TABLE_2 AS in0

)

SELECT *

FROM Reformat_3
