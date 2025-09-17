{{
  config({    
    "materialized": "table",
    "alias": "dest_analyst_parent",
    "database": "qa_team",
    "schema": "qa_database"
  })
}}

WITH all_type_partitioned_1 AS (

  SELECT * 
  
  FROM {{ source('qa_team.qa_database', 'all_type_partitioned') }}

),

Reformat_1 AS (

  SELECT 
    c_tinyint AS c_tinyint,
    c_smallint AS c_smallint,
    c_int AS c_int,
    c_bigint AS c_bigint,
    c_float AS c_float,
    c_double AS c_double,
    concat(c_string, '{{ var("c_project_int") }}') AS c_string,
    c_boolean AS c_boolean,
    c_array AS c_array,
    c_struct AS c_struct,
    p_int AS p_int,
    p_string AS p_string,
    {{ var('c_string_app') }} AS c_parameter_string
  
  FROM all_type_partitioned_1 AS in0

)

SELECT *

FROM Reformat_1
