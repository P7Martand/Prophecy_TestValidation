{{
  config({    
    "materialized": "ephemeral",
    "database": "qa_team",
    "schema": "qa_database"
  })
}}

WITH fsi_2022_download_xlsx_1 AS (

  SELECT *
  
  FROM {{ prophecy_tmp_source('parent_pipeline', 'fsi_2022_download_xlsx_1') }}

),

all_type_non_partitioned_different_rows_1 AS (

  SELECT *
  
  FROM {{ prophecy_tmp_source('parent_pipeline', 'all_type_non_partitioned_different_rows_1') }}

),

S9MB_annual_enterprise_survey_2023_financial_year_provisional_csv_1 AS (

  SELECT *
  
  FROM {{
    prophecy_tmp_source(
      'parent_pipeline', 
      'S9MB_annual_enterprise_survey_2023_financial_year_provisional_csv_1'
    )
  }}

),

SQLStatement_3 AS (

  SELECT *
  
  FROM all_type_non_partitioned_different_rows_1
  
  WHERE c_int != (
          (
            SELECT count(*)
            
            FROM fsi_2022_download_xlsx_1
           )
          + (
              SELECT count(*)
              
              FROM S9MB_annual_enterprise_survey_2023_financial_year_provisional_csv_1
             )
        )

),

all_type_partitioned_1 AS (

  SELECT * 
  
  FROM {{ source('qa_team.qa_database', 'all_type_partitioned') }}

),

Transpose_1 AS (

  {{
    DatabricksSqlBasics.Transpose(
      'all_type_partitioned_1', 
      [
        'c_smallint', 
        'c_int', 
        'c_bigint', 
        'c_float', 
        'c_tinyint', 
        'c_struct', 
        'c_array', 
        'c_boolean', 
        'p_string'
      ], 
      ['c_double', 'c_string'], 
      'Name', 
      'Value', 
      [
        'c_tinyint', 
        'c_smallint', 
        'c_int', 
        'c_bigint', 
        'c_float', 
        'c_double', 
        'c_string', 
        'c_boolean', 
        'c_array', 
        'c_struct', 
        'p_int', 
        'p_string'
      ]
    )
  }}

),

DynamicSelect_1 AS (

  {{
    DatabricksSqlBasics.DynamicSelect(
      'Transpose_1', 
      [
        { "name": "c_smallint", "dataType": "SmallInt" }, 
        { "name": "c_int", "dataType": "Integer" }, 
        { "name": "c_bigint", "dataType": "Bigint" }, 
        { "name": "c_float", "dataType": "Float" }, 
        { "name": "c_tinyint", "dataType": "TinyInt" }, 
        { "name": "c_struct", "dataType": "Struct" }, 
        { "name": "c_array", "dataType": "Array" }, 
        { "name": "c_boolean", "dataType": "Boolean" }, 
        { "name": "p_string", "dataType": "String" }, 
        { "name": "Name", "dataType": "String" }, 
        { "name": "Value", "dataType": "String" }
      ], 
      [
        "Boolean", 
        "String", 
        "Integer", 
        "Short", 
        "Byte", 
        "Long", 
        "Float", 
        "Decimal", 
        "Binary", 
        "Date", 
        "Timestamp", 
        "Struct"
      ], 
      'SELECT_FIELD_TYPES', 
      ""
    )
  }}

),

MultiColumnRename_1 AS (

  {{
    DatabricksSqlBasics.MultiColumnRename(
      'DynamicSelect_1', 
      ['c_int', 'c_float', 'Name', 'Value'], 
      'editPrefixSuffix', 
      ['c_int', 'c_float', 'c_struct', 'c_boolean', 'p_string', 'Name', 'Value'], 
      'Prefix', 
      'PRE_', 
      ""
    )
  }}

),

all_type_table_1 AS (

  SELECT *
  
  FROM {{ prophecy_tmp_source('parent_pipeline', 'all_type_table_1') }}

),

DataCleansing_1 AS (

  {{
    DatabricksSqlBasics.DataCleansing(
      'MultiColumnRename_1', 
      [
        { "name": "PRE_c_int", "dataType": "Integer" }, 
        { "name": "PRE_c_float", "dataType": "Float" }, 
        { "name": "c_struct", "dataType": "Struct" }, 
        { "name": "c_boolean", "dataType": "Boolean" }, 
        { "name": "p_string", "dataType": "String" }, 
        { "name": "PRE_Name", "dataType": "String" }, 
        { "name": "PRE_Value", "dataType": "String" }
      ], 
      'makeUppercase', 
      ['PRE_c_int', 'PRE_c_float', 'c_boolean', 'p_string', 'PRE_Name', 'PRE_Value'], 
      true, 
      'NA', 
      true, 
      0, 
      true, 
      true, 
      true, 
      true, 
      true, 
      true, 
      true, 
      false, 
      '1970-01-01', 
      false, 
      '1970-01-01 00:00:00.0'
    )
  }}

),

MultiColumnEdit_1 AS (

  {{
    DatabricksSqlBasics.MultiColumnEdit(
      'DataCleansing_1', 
      "concat(column_name, column_value)", 
      ['PRE_c_int', 'PRE_c_float', 'c_struct', 'c_boolean', 'p_string', 'PRE_Name', 'PRE_Value'], 
      ['PRE_c_int', 'PRE_c_float', 'c_boolean', 'p_string', 'PRE_Name', 'PRE_Value'], 
      true, 
      'Suffix', 
      '_suffix'
    )
  }}

),

UnionByName_1 AS (

  {{
    DatabricksSqlBasics.UnionByName(
      'MultiColumnEdit_1,MultiColumnEdit_1', 
      [
        [
          { "name": "PRE_c_int", "dataType": "Integer" }, 
          { "name": "PRE_c_float", "dataType": "Float" }, 
          { "name": "c_struct", "dataType": "Struct" }, 
          { "name": "c_boolean", "dataType": "Boolean" }, 
          { "name": "p_string", "dataType": "String" }, 
          { "name": "PRE_Name", "dataType": "String" }, 
          { "name": "PRE_Value", "dataType": "String" }, 
          { "name": "PRE_c_int_suffix", "dataType": "String" }, 
          { "name": "PRE_c_float_suffix", "dataType": "String" }, 
          { "name": "c_boolean_suffix", "dataType": "String" }, 
          { "name": "p_string_suffix", "dataType": "String" }, 
          { "name": "PRE_Name_suffix", "dataType": "String" }, 
          { "name": "PRE_Value_suffix", "dataType": "String" }
        ], 
        [
          { "name": "PRE_c_int", "dataType": "Integer" }, 
          { "name": "PRE_c_float", "dataType": "Float" }, 
          { "name": "c_struct", "dataType": "Struct" }, 
          { "name": "c_boolean", "dataType": "Boolean" }, 
          { "name": "p_string", "dataType": "String" }, 
          { "name": "PRE_Name", "dataType": "String" }, 
          { "name": "PRE_Value", "dataType": "String" }, 
          { "name": "PRE_c_int_suffix", "dataType": "String" }, 
          { "name": "PRE_c_float_suffix", "dataType": "String" }, 
          { "name": "c_boolean_suffix", "dataType": "String" }, 
          { "name": "p_string_suffix", "dataType": "String" }, 
          { "name": "PRE_Name_suffix", "dataType": "String" }, 
          { "name": "PRE_Value_suffix", "dataType": "String" }
        ]
      ], 
      'nameBasedUnionOperation'
    )
  }}

),

split_text_columns AS (

  {{
    DatabricksSqlBasics.TextToColumns(
      'UnionByName_1', 
      'p_string_suffix', 
      "a", 
      'splitRows', 
      1, 
      'Leave extra in last column', 
      'root', 
      'generated', 
      'generated_column'
    )
  }}

),

ALL_TYPE_TABLE_2 AS (

  SELECT *
  
  FROM {{ prophecy_tmp_source('parent_pipeline', 'ALL_TYPE_TABLE_2') }}

),

all_type_json_json_1 AS (

  SELECT *
  
  FROM {{ prophecy_tmp_source('parent_pipeline', 'all_type_json_json_1') }}

),

customer_data_with_details AS (

  SELECT *
  
  FROM {{ ref('parent_pipeline__customer_data_with_details')}}

),

FuzzyMatch_1 AS (

  {{
    DatabricksSqlBasics.FuzzyMatch(
      'split_text_columns', 
      'PURGE', 
      '', 
      'PRE_c_int', 
      { 'custom': ['PRE_c_float'], 'exact': ['c_boolean'], 'equals': ['PRE_Value_suffix'] }, 
      80, 
      false
    )
  }}

),

file_example_XLSX_5000_1 AS (

  SELECT *
  
  FROM {{ prophecy_tmp_source('parent_pipeline', 'file_example_XLSX_5000_1') }}

),

mongo_deepNestedData_1 AS (

  SELECT *
  
  FROM {{ prophecy_tmp_source('parent_pipeline', 'mongo_deepNestedData_1') }}

),

SQLStatement_2 AS (

  SELECT *
  
  FROM customer_data_with_details
  
  WHERE c_int != (
          (
            SELECT count(*)
            
            FROM mongo_deepNestedData_1
           )
          + (
              SELECT count(*)
              
              FROM all_type_table_1
             )
          + (
              SELECT count(*)
              
              FROM ALL_TYPE_TABLE_2
             )
          + (
              SELECT count(*)
              
              FROM file_example_XLSX_5000_1
             )
          + (
              SELECT count(*)
              
              FROM all_type_json_json_1
             )
          + (
              SELECT count(*)
              
              FROM SQLStatement_3
             )
          + (
              SELECT count(*)
              
              FROM FuzzyMatch_1
             )
        )

),

Limit_2 AS (

  SELECT * 
  
  FROM SQLStatement_2 AS in0
  
  LIMIT 10

)

SELECT *

FROM Limit_2
