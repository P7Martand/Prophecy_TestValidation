{{
  config({    
    "materialized": "table",
    "alias": "smatsheet_to_tables",
    "database": "qa_prakhar_database",
    "schema": "qa_schema"
  })
}}

WITH target_file_pr_1 AS (

  SELECT *
  
  FROM {{ prophecy_tmp_source('tmp_pipelines', 'target_file_pr_1') }}

),

concatenated_dates AS (

  SELECT 
    *,
    concat(Start_Date, End_Date) AS Total_Date
  
  FROM target_file_pr_1 AS in0

),

all_concatenated_dates AS (

  SELECT *
  
  FROM concatenated_dates

)

SELECT *

FROM all_concatenated_dates
