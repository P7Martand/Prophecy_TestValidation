{{
  config({    
    "materialized": "ephemeral",
    "database": "qa_team",
    "schema": "qa_database"
  })
}}

WITH s3_employee_details_csv AS (

  SELECT *
  
  FROM {{ prophecy_tmp_source('parent_pipeline', 's3_employee_details_csv') }}

),

DEST_ANALYST_PARENT_1 AS (

  SELECT * 
  
  FROM {{ source('qa_team.qa_database', 'dest_analyst_parent') }}

),

Filter_1 AS (

  SELECT * 
  
  FROM DEST_ANALYST_PARENT_1 AS in0
  
  WHERE c_parameter_string == {{ var('c_string_app') }}

),

SQLStatement_1 AS (

  SELECT *
  
  FROM Filter_1
  
  WHERE c_int != (
          SELECT (
                   CASE
                     WHEN COUNT(*) < 100
                       THEN RAISE_ERROR('Row count less than 100 buddy boy')
                     ELSE count(*)
                   END
                 ) AS result_comparison
          
          FROM Filter_1
         )

),

limited_partitioned_data AS (

  SELECT * 
  
  FROM SQLStatement_1 AS in0
  
  LIMIT 150

),

Limit_4 AS (

  SELECT * 
  
  FROM limited_partitioned_data AS in0
  
  LIMIT 10

),

basic_seed AS (

  SELECT * 
  
  FROM {{ ref('basic_seed')}}

),

Aggregate_1 AS (

  SELECT 
    any_value(c_int) AS c_int,
    any_value(c_boolean) AS c_boolean,
    any_value(c_string) AS c_string
  
  FROM basic_seed AS in0
  
  GROUP BY c_string
  
  HAVING c_string IS NOT NULL

),

WindowFunction_1 AS (

  SELECT 
    *,
    row_number() OVER (PARTITION BY c_int ORDER BY c_string ASC NULLS LAST, c_boolean DESC NULLS FIRST ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS c_string_0,
    row_number() OVER (PARTITION BY c_int ORDER BY c_string ASC NULLS LAST, c_boolean DESC NULLS FIRST ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS c_boolean_0
  
  FROM Aggregate_1 AS in0

),

OrderBy_1 AS (

  SELECT * 
  
  FROM WindowFunction_1 AS in0
  
  ORDER BY c_string ASC NULLS LAST, c_string_0 DESC, c_int ASC NULLS FIRST

),

Deduplicate_1 AS (

  SELECT * 
  
  FROM OrderBy_1 AS in0
  
  QUALIFY ROW_NUMBER() OVER (PARTITION BY c_int, c_boolean, c_string, c_string_0, c_boolean_0 ORDER BY concat(c_int, c_string) ASC NULLS LAST) = 1

),

Reformat_2 AS (

  SELECT 
    c_int AS c_int,
    c_boolean AS c_boolean,
    c_string AS c_string,
    c_string_0 AS c_string_0,
    c_boolean_0 AS c_boolean_0,
    ARRAY(1, 2, 3, 4) AS c_array_int,
    ARRAY(CAST(c_int AS STRING), CAST(c_boolean AS STRING), 'test') AS c_array_string
  
  FROM Deduplicate_1 AS in0

),

FlattenSchema_1 AS (

  SELECT 
    c_array_int.col AS c_array_int,
    c_array_string.col AS c_array_string,
    c_int AS c_int,
    c_boolean AS c_boolean,
    c_string AS c_string
  
  FROM Reformat_2 AS in0, 
  LATERAL explode_outer(c_array_int) AS c_array_int, 
  LATERAL explode_outer(c_array_string) AS c_array_string

),

Limit_3 AS (

  SELECT * 
  
  FROM FlattenSchema_1 AS in0
  
  LIMIT 10

),

customer_data_with_details AS (

  SELECT 
    in0.Name AS Name,
    in0.Age AS Age,
    in0.City AS City,
    in0.Salary AS Salary,
    in1.c_int AS c_int,
    in1.c_boolean AS c_boolean,
    in2.c_tinyint AS c_tinyint,
    in2.c_smallint AS c_smallint,
    in2.c_bigint AS c_bigint,
    in2.c_float AS c_float,
    in2.c_double AS c_double,
    CAST(in2.c_array AS STRING) AS c_array,
    CAST(in2.c_struct AS STRING) AS c_struct,
    in2.c_struct.state AS c_struct_state,
    in2.c_struct.pin AS c_struct_pin,
    in2.c_struct.city AS c_struct_city
  
  FROM s3_employee_details_csv AS in0
  INNER JOIN Limit_3 AS in1
     ON in0.Name != in1.c_string
  INNER JOIN Limit_4 AS in2
     ON in1.c_string != in2.c_struct.city

)

SELECT *

FROM customer_data_with_details
