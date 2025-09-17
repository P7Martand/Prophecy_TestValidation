Config = {
    "c_int": 2, 
    "c_string": "'dummy string value this is'", 
    "c_boolean": True, 
    "c_date": Date("current_date()"), 
    "c_sql_expression": expr(ARRAY(1, 2, 3, 4)), 
    "c_float": 1.2345, 
    "c_array_string": array("'test1'", "'test2'", "concat('test1', 3)"), 
    "c_string1": "'test'", 
    "c_int1": 2, 
    "c_boolean_1": True, 
    "c_double": 222.0, 
    "c_string_app": "'c_string_app'", 
    "c_s3_path_csv_pipe_separator": "'\' / datasets / orchestration_datasets / csv / valid / csv_pipe_separator.csv \''"
}
Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)
SensorSchedule = SensorSchedule(enabled = False)

with DAG(Config = Config, Schedule = Schedule, SensorSchedule = SensorSchedule):
    s3_employee_details_csv = Task(
        task_id = "s3_employee_details_csv", 
        component = "Dataset", 
        label = "s3_employee_details_csv", 
        table = {
          "name": "{{ prophecy_tmp_source('parent_pipeline', 's3_employee_details_csv') }}", 
          "sourceType": "UnreferencedSource"
        }
    )
    T_ALL_TYPE_TABLE_2 = Task(
        task_id = "T_ALL_TYPE_TABLE_2", 
        component = "OrchestrationTarget", 
        kind = "SnowflakeTarget", 
        connector = Connection(kind = "snowflake", id = "snowflake"), 
        format = {"category" : "table", "kind" : "snowflake", "properties" : {"kind" : "snowflake", "properties" : {}}}, 
        properties = {
          "tableFullName": {
            "database": {
              "type": "concat_operation", 
              "properties": {"elements" : [{"type" : "literal", "properties" : {"value" : "QA_DATABASE"}}]}
            }, 
            "schema": {
              "type": "concat_operation", 
              "properties": {"elements" : [{"type" : "literal", "properties" : {"value" : "QA_SIMPLE_SCHEMA"}}]}
            }, 
            "name": {
              "type": "concat_operation", 
              "properties": {
                "elements": [{"type" : "literal", "properties" : {"value" : "T_PARTIAL_DEST_ALL_TYPE_TABLE"}}]
              }
            }
          }
        }
    )
    S9MB_annual_enterprise_survey_2023_financial_year_provisional_csv_1 = SourceTask(
        task_id = "S9MB_annual_enterprise_survey_2023_financial_year_provisional_csv_1", 
        component = "OrchestrationSource", 
        kind = "DatabricksVolumeSource", 
        connector = Connection(kind = "databricks", authType = "pat", id = "dev_sql_databricks"), 
        format = CSVFormat(
          header = True, 
          schema = {
            "fields": [{"dataType" : {"type" : "int64"}, "name" : "Year"},                         {"dataType" : {"type" : "utf8"}, "name" : "Industry_aggregation_NZSIOC"},                         {"dataType" : {"type" : "utf8"}, "name" : "Industry_code_NZSIOC"},                         {"dataType" : {"type" : "utf8"}, "name" : "Industry_name_NZSIOC"},                         {"dataType" : {"type" : "utf8"}, "name" : "Units"},                         {"dataType" : {"type" : "utf8"}, "name" : "Variable_code"},                         {"dataType" : {"type" : "utf8"}, "name" : "Variable_name"},                         {"dataType" : {"type" : "utf8"}, "name" : "Variable_category"},                         {"dataType" : {"type" : "utf8"}, "name" : "Value"},                         {"dataType" : {"type" : "utf8"}, "name" : "Industry_code_ANZSIC06"}], 
            "providerType": "arrow"
          }, 
          separator = ","
        ), 
        filePath = "/Volumes/qa-team/qa_volume_external/qa_external_volume/orchestration_datasets/csv/9MB_annual-enterprise-survey-2023-financial-year-provisional.csv"
    )
    all_type_table_1 = Task(
        task_id = "all_type_table_1", 
        component = "Dataset", 
        label = "all_type_table_1", 
        table = {"name" : "{{ prophecy_tmp_source('parent_pipeline', 'all_type_table_1') }}", "sourceType" : "UnreferencedSource"}
    )
    parent_pipeline__Reformat_3 = Task(
        task_id = "parent_pipeline__Reformat_3", 
        component = "Model", 
        modelName = "parent_pipeline__Reformat_3"
    )
    ALL_TYPE_TABLE_2 = Task(
        task_id = "ALL_TYPE_TABLE_2", 
        component = "Dataset", 
        label = "ALL_TYPE_TABLE_2", 
        table = {"name" : "{{ prophecy_tmp_source('parent_pipeline', 'ALL_TYPE_TABLE_2') }}", "sourceType" : "UnreferencedSource"}
    )
    fsi_2022_download_xlsx_1 = Task(
        task_id = "fsi_2022_download_xlsx_1", 
        component = "Dataset", 
        label = "fsi_2022_download_xlsx_1", 
        table = {
          "name": "{{ prophecy_tmp_source('parent_pipeline', 'fsi_2022_download_xlsx_1') }}", 
          "sourceType": "UnreferencedSource"
        }
    )
    all_type_json_json_1 = Task(
        task_id = "all_type_json_json_1", 
        component = "Dataset", 
        label = "all_type_json_json_1", 
        table = {
          "name": "{{ prophecy_tmp_source('parent_pipeline', 'all_type_json_json_1') }}", 
          "sourceType": "UnreferencedSource"
        }
    )
    T_s3_target = Task(
        task_id = "T_s3_target", 
        component = "OrchestrationTarget", 
        kind = "S3Target", 
        connector = Connection(kind = "s3", id = "s3"), 
        format = {"category" : "file", "kind" : "csv", "properties" : {"header" : True, "separator" : ","}}, 
        properties = {
          "filePath": {
            "type": "concat_operation", 
            "properties": {
              "elements": [{
                              "type": "literal", 
                              "properties": {
                                "value": "/datasets/orchestration_datasets/csv/target/csv_pipe_separator.csv"
                              }
                            }]
            }
          }
        }
    )
    T_all_type_table_1 = Task(
        task_id = "T_all_type_table_1", 
        component = "OrchestrationTarget", 
        kind = "MSSQLTarget", 
        connector = Connection(kind = "mssql", id = "mssql"), 
        format = {"category" : "table", "kind" : "mssql", "properties" : {"kind" : "mssql", "properties" : {}}}, 
        properties = {
          "tableFullName": {
            "database": {
              "type": "concat_operation", 
              "properties": {"elements" : [{"type" : "literal", "properties" : {"value" : "qa_performance"}}]}
            }, 
            "schema": {
              "type": "concat_operation", 
              "properties": {"elements" : [{"type" : "literal", "properties" : {"value" : "qa_schema"}}]}
            }, 
            "name": {
              "type": "concat_operation", 
              "properties": {"elements" : [{"type" : "literal", "properties" : {"value" : "dest_all_type_table"}}]}
            }
          }
        }
    )
    T_S9MB_annual_enterprise_survey_2023_financial_year_provisional_csv_1 = Task(
        task_id = "T_S9MB_annual_enterprise_survey_2023_financial_year_provisional_csv_1", 
        component = "OrchestrationTarget", 
        kind = "DatabricksVolumeTarget", 
        connector = Connection(kind = "databricks", id = "dev_sql_databricks"), 
        format = {"category" : "file", "kind" : "csv", "properties" : {"header" : True, "separator" : ","}}, 
        properties = {
          "filePath": {
            "type": "concat_operation", 
            "properties": {
              "elements": [{
                              "type": "literal", 
                              "properties": {
                                "value": "/Volumes/qa-team/qa_volume_external/qa_external_volume/orchestration_datasets/target/9MB_annual-enterprise-survey-2023-financial-year-provisional.csv"
                              }
                            }]
            }
          }
        }
    )
    all_type_json_json_1 = SourceTask(
        task_id = "all_type_json_json_1", 
        component = "OrchestrationSource", 
        kind = "SharepointSource", 
        connector = Connection(kind = "sharepoint", id = "sharepoint"), 
        format = JSONFormat(
          multiDoc = False, 
          schema = {
            "fields": [{"dataType" : {"dataType" : {"type" : "float64"}, "type" : "Array"}, "name" : "c_array_of_floats"},                         {"dataType" : {"dataType" : {"type" : "utf8"}, "type" : "Array"}, "name" : "c_array_of_arrays"},                         {
                          "dataType": {
                            "dataType": {
                              "fields": [{"dataType" : {"type" : "float64"}, "name" : "id"},                                           {"dataType" : {"type" : "utf8"}, "name" : "name"},                                           {"dataType" : {"type" : "bool"}, "name" : "active"}], 
                              "type": "Struct"
                            }, 
                            "type": "Array"
                          }, 
                          "name": "c_array_of_structs"
                        },                         {
                          "dataType": {
                            "fields": [{
                                          "dataType": {
                                            "fields": [{
                                                          "dataType": {"type" : "float64"}, 
                                                          "name": "deeply_nested_number"
                                                        },                                                         {
                                                          "dataType": {"dataType" : {"type" : "bool"}, "type" : "Array"}, 
                                                          "name": "deeply_nested_array"
                                                        },                                                         {
                                                          "dataType": {
                                                            "fields": [{
                                                                          "dataType": {"type" : "utf8"}, 
                                                                          "name": "final_key"
                                                                        },                                                                         {
                                                                          "dataType": {
                                                                            "fields": [{
                                                                                          "dataType": {
                                                                                            "type": "date32"
                                                                                          }, 
                                                                                          "name": "date"
                                                                                        },                                                                                         {
                                                                                          "dataType": {"type" : "utf8"}, 
                                                                                          "name": "time"
                                                                                        },                                                                                         {
                                                                                          "dataType": {
                                                                                            "type": "timestamp"
                                                                                          }, 
                                                                                          "name": "datetime"
                                                                                        }], 
                                                                            "type": "Struct"
                                                                          }, 
                                                                          "name": "more_nested"
                                                                        }], 
                                                            "type": "Struct"
                                                          }, 
                                                          "name": "deeply_nested_object"
                                                        },                                                         {"dataType" : {"type" : "utf8"}, "name" : "deeply_nested_string"}], 
                                            "type": "Struct"
                                          }, 
                                          "name": "c_nested_struct"
                                        },                                         {"dataType" : {"type" : "float64"}, "name" : "nested_number"},                                         {"dataType" : {"type" : "float64"}, "name" : "nested_float"},                                         {"dataType" : {"type" : "utf8"}, "name" : "nested_null"},                                         {"dataType" : {"type" : "date32"}, "name" : "nested_date"},                                         {"dataType" : {"type" : "utf8"}, "name" : "nested_time"},                                         {"dataType" : {"type" : "timestamp"}, "name" : "nested_datetime"},                                         {"dataType" : {"type" : "utf8"}, "name" : "nested_string"},                                         {"dataType" : {"type" : "bool"}, "name" : "nested_boolean"},                                         {
                                          "dataType": {"dataType" : {"type" : "float64"}, "type" : "Array"}, 
                                          "name": "nested_array"
                                        },                                         {
                                          "dataType": {
                                            "dataType": {
                                              "fields": [{"dataType" : {"type" : "utf8"}, "name" : "key"},                                                           {"dataType" : {"type" : "bool"}, "name" : "flag"}], 
                                              "type": "Struct"
                                            }, 
                                            "type": "Array"
                                          }, 
                                          "name": "nested_array_of_structs"
                                        }], 
                            "type": "Struct"
                          }, 
                          "name": "c_struct"
                        },                         {"dataType" : {"type" : "float64"}, "name" : "c_number"},                         {"dataType" : {"type" : "timestamp"}, "name" : "c_datetime"},                         {"dataType" : {"dataType" : {"type" : "bool"}, "type" : "Array"}, "name" : "c_array_of_booleans"},                         {"dataType" : {"dataType" : {"type" : "utf8"}, "type" : "Array"}, "name" : "c_array_of_strings"},                         {"dataType" : {"type" : "float64"}, "name" : "c_float"},                         {"dataType" : {"type" : "bool"}, "name" : "c_boolean"},                         {
                          "dataType": {
                            "fields": [{"dataType" : {"type" : "utf8"}, "name" : "c_time"},                                         {"dataType" : {"type" : "timestamp"}, "name" : "c_datetime"},                                         {
                                          "dataType": {"dataType" : {"type" : "float64"}, "type" : "Array"}, 
                                          "name": "c_array_of_numbers"
                                        },                                         {"dataType" : {"type" : "float64"}, "name" : "c_float"},                                         {"dataType" : {"type" : "date32"}, "name" : "c_date"},                                         {
                                          "dataType": {"dataType" : {"type" : "float64"}, "type" : "Array"}, 
                                          "name": "c_array_of_floats"
                                        },                                         {
                                          "dataType": {"dataType" : {"type" : "bool"}, "type" : "Array"}, 
                                          "name": "c_array_of_booleans"
                                        },                                         {
                                          "dataType": {"dataType" : {"type" : "utf8"}, "type" : "Array"}, 
                                          "name": "c_array_of_arrays"
                                        },                                         {"dataType" : {"type" : "float64"}, "name" : "c_number"},                                         {"dataType" : {"type" : "bool"}, "name" : "c_boolean"},                                         {"dataType" : {"type" : "utf8"}, "name" : "c_null_value"},                                         {
                                          "dataType": {
                                            "fields": [{"dataType" : {"type" : "utf8"}, "name" : "nested_null"},                                                         {"dataType" : {"type" : "date32"}, "name" : "nested_date"},                                                         {"dataType" : {"type" : "timestamp"}, "name" : "nested_datetime"},                                                         {
                                                          "dataType": {
                                                            "fields": [{
                                                                          "dataType": {"type" : "utf8"}, 
                                                                          "name": "deeply_nested_string"
                                                                        },                                                                         {
                                                                          "dataType": {"type" : "float64"}, 
                                                                          "name": "deeply_nested_number"
                                                                        },                                                                         {
                                                                          "dataType": {
                                                                            "dataType": {"type" : "bool"}, 
                                                                            "type": "Array"
                                                                          }, 
                                                                          "name": "deeply_nested_array"
                                                                        },                                                                         {
                                                                          "dataType": {
                                                                            "fields": [{
                                                                                          "dataType": {"type" : "utf8"}, 
                                                                                          "name": "final_key"
                                                                                        },                                                                                         {
                                                                                          "dataType": {
                                                                                            "fields": [{
                                                                                                          "dataType": {
                                                                                                            "type": "utf8"
                                                                                                          }, 
                                                                                                          "name": "time"
                                                                                                        },                                                                                                         {
                                                                                                          "dataType": {
                                                                                                            "type": "timestamp"
                                                                                                          }, 
                                                                                                          "name": "datetime"
                                                                                                        },                                                                                                         {
                                                                                                          "dataType": {
                                                                                                            "type": "date32"
                                                                                                          }, 
                                                                                                          "name": "date"
                                                                                                        }], 
                                                                                            "type": "Struct"
                                                                                          }, 
                                                                                          "name": "more_nested"
                                                                                        }], 
                                                                            "type": "Struct"
                                                                          }, 
                                                                          "name": "deeply_nested_object"
                                                                        }], 
                                                            "type": "Struct"
                                                          }, 
                                                          "name": "c_nested_struct"
                                                        },                                                         {"dataType" : {"type" : "float64"}, "name" : "nested_number"},                                                         {"dataType" : {"type" : "float64"}, "name" : "nested_float"},                                                         {"dataType" : {"type" : "utf8"}, "name" : "nested_time"},                                                         {
                                                          "dataType": {
                                                            "dataType": {"type" : "float64"}, 
                                                            "type": "Array"
                                                          }, 
                                                          "name": "nested_array"
                                                        },                                                         {
                                                          "dataType": {
                                                            "dataType": {
                                                              "fields": [{"dataType" : {"type" : "utf8"}, "name" : "key"},                                                                           {"dataType" : {"type" : "bool"}, "name" : "flag"}], 
                                                              "type": "Struct"
                                                            }, 
                                                            "type": "Array"
                                                          }, 
                                                          "name": "nested_array_of_structs"
                                                        },                                                         {"dataType" : {"type" : "utf8"}, "name" : "nested_string"},                                                         {"dataType" : {"type" : "bool"}, "name" : "nested_boolean"}], 
                                            "type": "Struct"
                                          }, 
                                          "name": "c_struct"
                                        },                                         {
                                          "dataType": {"dataType" : {"type" : "utf8"}, "type" : "Array"}, 
                                          "name": "c_array_of_strings"
                                        },                                         {
                                          "dataType": {
                                            "dataType": {
                                              "fields": [{"dataType" : {"type" : "float64"}, "name" : "id"},                                                           {"dataType" : {"type" : "utf8"}, "name" : "name"},                                                           {"dataType" : {"type" : "bool"}, "name" : "active"}], 
                                              "type": "Struct"
                                            }, 
                                            "type": "Array"
                                          }, 
                                          "name": "c_array_of_structs"
                                        },                                         {"dataType" : {"type" : "float64"}, "name" : "c_int"},                                         {"dataType" : {"type" : "utf8"}, "name" : "c_string"}], 
                            "type": "Struct"
                          }, 
                          "name": "c_very_complex"
                        },                         {"dataType" : {"type" : "utf8"}, "name" : "c_string"},                         {"dataType" : {"dataType" : {"type" : "float64"}, "type" : "Array"}, "name" : "c_array_of_numbers"},                         {"dataType" : {"type" : "date32"}, "name" : "c_date"},                         {"dataType" : {"type" : "utf8"}, "name" : "c_time"},                         {"dataType" : {"type" : "float64"}, "name" : "c_int"},                         {"dataType" : {"type" : "utf8"}, "name" : "c_null_value"}], 
            "providerType": "arrow"
          }
        ), 
        filePath = "/qa_datasets/orchestration_datasets/json/dict/valid/all_type_json.json"
    )
    T_mongo_deepNestedData_1 = Task(
        task_id = "T_mongo_deepNestedData_1", 
        component = "OrchestrationTarget", 
        kind = "MongoDBTarget", 
        connector = Connection(kind = "mongodb", id = "mongodb"), 
        format = {"category" : "table", "kind" : "mongodb", "properties" : {"kind" : "mongodb", "properties" : {}}}, 
        properties = {
          "tableFullName": {
            "schema": "default", 
            "database": {
              "type": "concat_operation", 
              "properties": {"elements" : [{"type" : "literal", "properties" : {"value" : "admin"}}]}
            }, 
            "name": {
              "type": "concat_operation", 
              "properties": {"elements" : [{"type" : "literal", "properties" : {"value" : "target_deepNestedData"}}]}
            }
          }
        }
    )
    all_type_non_partitioned_different_rows_1 = Task(
        task_id = "all_type_non_partitioned_different_rows_1", 
        component = "Dataset", 
        label = "all_type_non_partitioned_different_rows_1", 
        table = {
          "name": "{{ prophecy_tmp_source('parent_pipeline', 'all_type_non_partitioned_different_rows_1') }}", 
          "sourceType": "UnreferencedSource"
        }
    )
    S9MB_annual_enterprise_survey_2023_financial_year_provisional_csv_1 = Task(
        task_id = "S9MB_annual_enterprise_survey_2023_financial_year_provisional_csv_1", 
        component = "Dataset", 
        label = "S9MB_annual_enterprise_survey_2023_financial_year_provisional_csv_1", 
        table = {
          "name": "{{ prophecy_tmp_source('parent_pipeline', 'S9MB_annual_enterprise_survey_2023_financial_year_provisional_csv_1') }}", 
          "sourceType": "UnreferencedSource"
        }
    )
    mongo_deepNestedData_1 = SourceTask(
        task_id = "mongo_deepNestedData_1", 
        component = "OrchestrationSource", 
        kind = "MongoDBSource", 
        connector = Connection(
          kind = "mongodb", 
          database = "", 
          collection = "", 
          username = "", 
          host = "", 
          id = "mongodb", 
          protocol = ""
        ), 
        format = MONGODBFormat(
          additionalProperties = {"copilot" : {"datasetDescriptionStatus" : "fromCopilot"}}, 
          description = "Comprehensive user profiles encompassing personal information, contact details, and address history, enabling enhanced customer relationship management and targeted outreach.", 
          schema = {
            "fields": [{
                          "dataType": {"type" : "utf8"}, 
                          "description": "Unique identifier for the user account", 
                          "name": "_id"
                        },                         {
                          "dataType": {
                            "fields": [{
                                          "dataType": {"type" : "timestamp"}, 
                                          "description": "Timestamp indicating when the account was created", 
                                          "name": "created"
                                        },                                         {
                                          "dataType": {"type" : "timestamp"}, 
                                          "description": "Timestamp of the user's last login", 
                                          "name": "lastLogin"
                                        },                                         {
                                          "dataType": {
                                            "fields": [{
                                                          "dataType": {
                                                            "fields": [{
                                                                          "dataType": {"type" : "bool"}, 
                                                                          "description": "Flag indicating if email notifications are enabled", 
                                                                          "name": "email"
                                                                        },                                                                         {
                                                                          "dataType": {
                                                                            "fields": [{
                                                                                          "dataType": {"type" : "bool"}, 
                                                                                          "description": "Flag indicating if push notifications are enabled", 
                                                                                          "name": "enabled"
                                                                                        },                                                                                         {
                                                                                          "dataType": {
                                                                                            "dataType": {
                                                                                              "fields": [{
                                                                                                            "dataType": {
                                                                                                              "type": "utf8"
                                                                                                            }, 
                                                                                                            "description": "The application name for which the notification exception is set", 
                                                                                                            "name": "app"
                                                                                                          },                                                                                                           {
                                                                                                            "dataType": {
                                                                                                              "type": "bool"
                                                                                                            }, 
                                                                                                            "description": "Indicates whether notifications for the specific app are muted", 
                                                                                                            "name": "muted"
                                                                                                          },                                                                                                           {
                                                                                                            "dataType": {
                                                                                                              "type": "timestamp"
                                                                                                            }, 
                                                                                                            "description": "Timestamp indicating until when notifications are muted for the specific app", 
                                                                                                            "name": "mutedUntil"
                                                                                                          }], 
                                                                                              "type": "Struct"
                                                                                            }, 
                                                                                            "type": "Array"
                                                                                          }, 
                                                                                          "description": "List of exceptions for push notifications", 
                                                                                          "name": "exceptions"
                                                                                        },                                                                                         {
                                                                                          "dataType": {"type" : "utf8"}, 
                                                                                          "description": "Sound setting for push notifications", 
                                                                                          "name": "sound"
                                                                                        }], 
                                                                            "type": "Struct"
                                                                          }, 
                                                                          "description": "Settings related to push notifications", 
                                                                          "name": "push"
                                                                        },                                                                         {
                                                                          "dataType": {"type" : "bool"}, 
                                                                          "description": "Indicates whether SMS notifications are enabled", 
                                                                          "name": "sms"
                                                                        }], 
                                                            "type": "Struct"
                                                          }, 
                                                          "description": "Notification settings for the user's account", 
                                                          "name": "notifications"
                                                        },                                                         {
                                                          "dataType": {
                                                            "fields": [{
                                                                          "dataType": {
                                                                            "dataType": {
                                                                              "fields": [{
                                                                                            "dataType": {
                                                                                              "type": "utf8"
                                                                                            }, 
                                                                                            "description": "Unique identifier for each authorized device", 
                                                                                            "name": "deviceId"
                                                                                          },                                                                                           {
                                                                                            "dataType": {
                                                                                              "type": "utf8"
                                                                                            }, 
                                                                                            "description": "Operating system of the authorized device", 
                                                                                            "name": "os"
                                                                                          },                                                                                           {
                                                                                            "dataType": {
                                                                                              "type": "timestamp"
                                                                                            }, 
                                                                                            "description": "Timestamp indicating when the device was registered", 
                                                                                            "name": "registeredOn"
                                                                                          },                                                                                           {
                                                                                            "dataType": {
                                                                                              "type": "utf8"
                                                                                            }, 
                                                                                            "description": "Type of the authentication device used by the user", 
                                                                                            "name": "type"
                                                                                          }], 
                                                                              "type": "Struct"
                                                                            }, 
                                                                            "type": "Array"
                                                                          }, 
                                                                          "description": "List of devices authorized for account access", 
                                                                          "name": "authDevices"
                                                                        },                                                                         {
                                                                          "dataType": {
                                                                            "dataType": {"type" : "utf8"}, 
                                                                            "type": "Array"
                                                                          }, 
                                                                          "description": "Backup codes available for account recovery", 
                                                                          "name": "backupCodes"
                                                                        },                                                                         {
                                                                          "dataType": {"type" : "bool"}, 
                                                                          "description": "Flag indicating if multi-factor authentication is enabled", 
                                                                          "name": "mfa"
                                                                        }], 
                                                            "type": "Struct"
                                                          }, 
                                                          "description": "Security settings related to user account protection", 
                                                          "name": "security"
                                                        },                                                         {
                                                          "dataType": {"type" : "utf8"}, 
                                                          "description": "User's selected theme for the account interface", 
                                                          "name": "theme"
                                                        }], 
                                            "type": "Struct"
                                          }, 
                                          "description": "Structure containing user-specific settings for the account", 
                                          "name": "settings"
                                        }], 
                            "type": "Struct"
                          }, 
                          "description": "Structure containing account-related information", 
                          "name": "account"
                        },                         {
                          "dataType": {
                            "fields": [{
                                          "dataType": {
                                            "dataType": {
                                              "fields": [{
                                                            "dataType": {
                                                              "fields": [{
                                                                            "dataType": {"type" : "utf8"}, 
                                                                            "description": "City of the user's home address", 
                                                                            "name": "city"
                                                                          },                                                                           {
                                                                            "dataType": {
                                                                              "fields": [{
                                                                                            "dataType": {
                                                                                              "dataType": {
                                                                                                "fields": [{
                                                                                                              "dataType": {
                                                                                                                "type": "timestamp"
                                                                                                              }, 
                                                                                                              "description": "Timestamp indicating when the location was last moved to", 
                                                                                                              "name": "movedOn"
                                                                                                            },                                                                                                             {
                                                                                                              "dataType": {
                                                                                                                "type": "float64"
                                                                                                              }, 
                                                                                                              "description": "Previous latitude of the user's home location", 
                                                                                                              "name": "oldLat"
                                                                                                            },                                                                                                             {
                                                                                                              "dataType": {
                                                                                                                "type": "float64"
                                                                                                              }, 
                                                                                                              "description": "Previous longitude of the user's home location", 
                                                                                                              "name": "oldLng"
                                                                                                            }], 
                                                                                                "type": "Struct"
                                                                                              }, 
                                                                                              "type": "Array"
                                                                                            }, 
                                                                                            "description": "History of changes to the geographical location of the user's home address", 
                                                                                            "name": "history"
                                                                                          },                                                                                           {
                                                                                            "dataType": {
                                                                                              "type": "float64"
                                                                                            }, 
                                                                                            "description": "Current latitude of the user's home location", 
                                                                                            "name": "lat"
                                                                                          },                                                                                           {
                                                                                            "dataType": {
                                                                                              "type": "float64"
                                                                                            }, 
                                                                                            "description": "Current longitude of the user's home location", 
                                                                                            "name": "lng"
                                                                                          }], 
                                                                              "type": "Struct"
                                                                            }, 
                                                                            "description": "Geographical coordinates of the user's home address", 
                                                                            "name": "geo"
                                                                          },                                                                           {
                                                                            "dataType": {
                                                                              "dataType": {
                                                                                "fields": [{
                                                                                              "dataType": {
                                                                                                "type": "timestamp"
                                                                                              }, 
                                                                                              "description": "Timestamp indicating when a resident moved into the home", 
                                                                                              "name": "movedIn"
                                                                                            },                                                                                             {
                                                                                              "dataType": {
                                                                                                "type": "utf8"
                                                                                              }, 
                                                                                              "description": "Name of the resident living at the user's home address", 
                                                                                              "name": "name"
                                                                                            },                                                                                             {
                                                                                              "dataType": {
                                                                                                "type": "utf8"
                                                                                              }, 
                                                                                              "description": "Relationship of the resident to the user", 
                                                                                              "name": "relation"
                                                                                            }], 
                                                                                "type": "Struct"
                                                                              }, 
                                                                              "type": "Array"
                                                                            }, 
                                                                            "description": "List of residents living at the user's home address", 
                                                                            "name": "residents"
                                                                          },                                                                           {
                                                                            "dataType": {"type" : "utf8"}, 
                                                                            "description": "State where the user's home address is located", 
                                                                            "name": "state"
                                                                          },                                                                           {
                                                                            "dataType": {"type" : "utf8"}, 
                                                                            "description": "Street address of the user's home", 
                                                                            "name": "street"
                                                                          },                                                                           {
                                                                            "dataType": {"type" : "utf8"}, 
                                                                            "description": "ZIP code of the user's home address", 
                                                                            "name": "zip"
                                                                          }], 
                                                              "type": "Struct"
                                                            }, 
                                                            "description": "Home address details of the user", 
                                                            "name": "home"
                                                          }], 
                                              "type": "Struct"
                                            }, 
                                            "type": "Array"
                                          }, 
                                          "description": "List of addresses associated with the user", 
                                          "name": "addresses"
                                        },                                         {
                                          "dataType": {
                                            "fields": [{
                                                          "dataType": {
                                                            "dataType": {
                                                              "fields": [{
                                                                            "dataType": {"type" : "utf8"}, 
                                                                            "description": "Email address of the user", 
                                                                            "name": "address"
                                                                          },                                                                           {
                                                                            "dataType": {
                                                                              "dataType": {
                                                                                "fields": [{
                                                                                              "dataType": {
                                                                                                "type": "timestamp"
                                                                                              }, 
                                                                                              "description": "Timestamp indicating when the email address was changed", 
                                                                                              "name": "changedOn"
                                                                                            },                                                                                             {
                                                                                              "dataType": {
                                                                                                "type": "utf8"
                                                                                              }, 
                                                                                              "description": "Previous email address before the most recent change", 
                                                                                              "name": "oldAddress"
                                                                                            }], 
                                                                                "type": "Struct"
                                                                              }, 
                                                                              "type": "Array"
                                                                            }, 
                                                                            "description": "History of changes made to the user's email addresses", 
                                                                            "name": "history"
                                                                          },                                                                           {
                                                                            "dataType": {"type" : "utf8"}, 
                                                                            "description": "Type of the email address (e.g., personal, work)", 
                                                                            "name": "type"
                                                                          },                                                                           {
                                                                            "dataType": {"type" : "bool"}, 
                                                                            "description": "Indicates whether the email address has been verified", 
                                                                            "name": "verified"
                                                                          }], 
                                                              "type": "Struct"
                                                            }, 
                                                            "type": "Array"
                                                          }, 
                                                          "description": "List of email addresses associated with the user", 
                                                          "name": "emails"
                                                        },                                                         {
                                                          "dataType": {
                                                            "dataType": {
                                                              "fields": [{
                                                                            "dataType": {
                                                                              "dataType": {
                                                                                "fields": [{
                                                                                              "dataType": {
                                                                                                "type": "utf8"
                                                                                              }, 
                                                                                              "description": "Unique identifier for each linked device", 
                                                                                              "name": "deviceId"
                                                                                            },                                                                                             {
                                                                                              "dataType": {
                                                                                                "type": "timestamp"
                                                                                              }, 
                                                                                              "description": "Timestamp of the last time the linked device was used", 
                                                                                              "name": "lastUsed"
                                                                                            },                                                                                             {
                                                                                              "dataType": {
                                                                                                "type": "utf8"
                                                                                              }, 
                                                                                              "description": "Model of the linked device", 
                                                                                              "name": "model"
                                                                                            }], 
                                                                                "type": "Struct"
                                                                              }, 
                                                                              "type": "Array"
                                                                            }, 
                                                                            "description": "Devices linked to the user's phone numbers", 
                                                                            "name": "linkedDevices"
                                                                          },                                                                           {
                                                                            "dataType": {"type" : "utf8"}, 
                                                                            "description": "Phone number associated with the user", 
                                                                            "name": "number"
                                                                          },                                                                           {
                                                                            "dataType": {"type" : "utf8"}, 
                                                                            "description": "Type of phone number (e.g., mobile, home)", 
                                                                            "name": "type"
                                                                          },                                                                           {
                                                                            "dataType": {"type" : "bool"}, 
                                                                            "description": "Indicates whether the phone number has been verified", 
                                                                            "name": "verified"
                                                                          }], 
                                                              "type": "Struct"
                                                            }, 
                                                            "type": "Array"
                                                          }, 
                                                          "description": "List of phone numbers associated with the user", 
                                                          "name": "phones"
                                                        }], 
                                            "type": "Struct"
                                          }, 
                                          "description": "Contact information associated with the user", 
                                          "name": "contact"
                                        },                                         {
                                          "dataType": {"type" : "int32"}, 
                                          "description": "Unique identifier for the user", 
                                          "name": "id"
                                        },                                         {
                                          "dataType": {
                                            "fields": [{
                                                          "dataType": {
                                                            "dataType": {
                                                              "fields": [{
                                                                            "dataType": {
                                                                              "dataType": {
                                                                                "fields": [{
                                                                                              "dataType": {
                                                                                                "type": "timestamp"
                                                                                              }, 
                                                                                              "description": "Timestamp indicating when the alias change occurred", 
                                                                                              "name": "changedOn"
                                                                                            },                                                                                             {
                                                                                              "dataType": {
                                                                                                "type": "utf8"
                                                                                              }, 
                                                                                              "description": "The previous nickname used by the user before the change", 
                                                                                              "name": "previousNickname"
                                                                                            }], 
                                                                                "type": "Struct"
                                                                              }, 
                                                                              "type": "Array"
                                                                            }, 
                                                                            "description": "History of changes made to the user's aliases", 
                                                                            "name": "history"
                                                                          },                                                                           {
                                                                            "dataType": {"type" : "utf8"}, 
                                                                            "description": "The current nickname of the user", 
                                                                            "name": "nickname"
                                                                          },                                                                           {
                                                                            "dataType": {"type" : "timestamp"}, 
                                                                            "description": "Timestamp indicating when the alias was first used", 
                                                                            "name": "usedSince"
                                                                          }], 
                                                              "type": "Struct"
                                                            }, 
                                                            "type": "Array"
                                                          }, 
                                                          "description": "List of alternative names or nicknames used by the user", 
                                                          "name": "aliases"
                                                        },                                                         {
                                                          "dataType": {"type" : "utf8"}, 
                                                          "description": "User's first name", 
                                                          "name": "first"
                                                        },                                                         {
                                                          "dataType": {"type" : "utf8"}, 
                                                          "description": "User's last name", 
                                                          "name": "last"
                                                        }], 
                                            "type": "Struct"
                                          }, 
                                          "description": "User's name details including first and last names", 
                                          "name": "name"
                                        }], 
                            "type": "Struct"
                          }, 
                          "description": "User profile information including contact details and addresses", 
                          "name": "user"
                        }], 
            "providerType": "Arrow"
          }
        ), 
        tableFullName = {"database" : "admin", "name" : "deepNestedData", "schema" : "default"}
    )
    T_file_example_XLSX_5000_1 = Task(
        task_id = "T_file_example_XLSX_5000_1", 
        component = "OrchestrationTarget", 
        kind = "SmartsheetTarget", 
        connector = Connection(kind = "smartsheet", id = "smartsheet"), 
        properties = {
          "filePath": {
            "type": "concat_operation", 
            "properties": {
              "elements": [{
                              "type": "literal", 
                              "properties": {"value" : "/QA Project/target/random_testfile_example_XLSX_5000"}
                            }]
            }
          }
        }, 
        format = {"properties" : {"header" : True}, "kind" : "smartsheet", "category" : "file"}
    )
    ALL_TYPE_TABLE_2 = SourceTask(
        task_id = "ALL_TYPE_TABLE_2", 
        component = "OrchestrationSource", 
        kind = "SnowflakeSource", 
        connector = Connection(
          kind = "snowflake", 
          database = "", 
          role = "", 
          username = "", 
          authType = "pwd", 
          id = "snowflake", 
          schema = "", 
          account = "", 
          warehouse = "", 
          password = None
        ), 
        format = SNOWFLAKEFormat(
          schema = {
            "fields": [{"dataType" : {"type" : "int16"}, "name" : "C_NUM"},                         {"dataType" : {"type" : "float64"}, "name" : "C_NUM10"},                         {"dataType" : {"type" : "float64"}, "name" : "C_DEC"},                         {"dataType" : {"type" : "float64"}, "name" : "C_NUMERIC"},                         {"dataType" : {"type" : "int16"}, "name" : "C_INT"},                         {"dataType" : {"type" : "int32"}, "name" : "C_INTEGER"},                         {"dataType" : {"type" : "float64"}, "name" : "C_DOUBLE"},                         {"dataType" : {"type" : "float64"}, "name" : "C_FLOAT"},                         {"dataType" : {"type" : "float64"}, "name" : "C_COUBLE_PRECISION"},                         {"dataType" : {"type" : "float64"}, "name" : "C_REAL"},                         {"dataType" : {"type" : "utf8"}, "name" : "C_VARCHAR"},                         {"dataType" : {"type" : "utf8"}, "name" : "C_VARCHAR50"},                         {"dataType" : {"type" : "utf8"}, "name" : "C_CHAR"},                         {"dataType" : {"type" : "utf8"}, "name" : "C_CHAR10"},                         {"dataType" : {"type" : "utf8"}, "name" : "C_STRING"},                         {"dataType" : {"type" : "utf8"}, "name" : "C_STRING20"},                         {"dataType" : {"type" : "utf8"}, "name" : "C_TEXT"},                         {"dataType" : {"type" : "utf8"}, "name" : "C_TEXT30"},                         {"dataType" : {"type" : "binary"}, "name" : "C_BINARY"},                         {"dataType" : {"type" : "binary"}, "name" : "C_BINARY100"},                         {"dataType" : {"type" : "binary"}, "name" : "C_VARBINARY"},                         {"dataType" : {"type" : "bool"}, "name" : "C_BOOL"},                         {"dataType" : {"type" : "timestamp"}, "name" : "C_TIMESTAMP"},                         {"dataType" : {"type" : "date32"}, "name" : "C_DATE"},                         {"dataType" : {"type" : "timestamp"}, "name" : "C_DATETIME"},                         {"dataType" : {"type" : "time64"}, "name" : "C_TIME"},                         {"dataType" : {"type" : "timestamp"}, "name" : "C_TIMESTAMPLTZ"},                         {"dataType" : {"type" : "timestamp"}, "name" : "C_TIMESTAMP_NTZ"},                         {"dataType" : {"type" : "utf8"}, "name" : "C_VARIANT"},                         {"dataType" : {"type" : "utf8"}, "name" : "C_ARRAY"},                         {"dataType" : {"type" : "utf8"}, "name" : "C_OBJECT"},                         {"dataType" : {"type" : "utf8"}, "name" : "C_GEOGRAPHY"}], 
            "providerType": "arrow"
          }
        ), 
        tableFullName = {"database" : "QA_DATABASE", "name" : "ALL_TYPE_TABLE", "schema" : "QA_SIMPLE_SCHEMA"}
    )
    parent_pipeline__customer_data_with_details = Task(
        task_id = "parent_pipeline__customer_data_with_details", 
        component = "Model", 
        modelName = "parent_pipeline__customer_data_with_details"
    )
    s3_employee_details_csv = SourceTask(
        task_id = "s3_employee_details_csv", 
        component = "OrchestrationSource", 
        kind = "S3Source", 
        connector = Connection(kind = "s3", id = "s3"), 
        format = CSVFormat(
          header = True, 
          schema = {
            "fields": [{"dataType" : {"type" : "utf8"}, "description" : "The name of the individual", "name" : "Name"},                         {"dataType" : {"type" : "int64"}, "description" : "The age of the individual", "name" : "Age"},                         {
                          "dataType": {"type" : "utf8"}, 
                          "description": "The city where the individual resides", 
                          "name": "City"
                        },                         {
                          "dataType": {"type" : "float64"}, 
                          "description": "The income amount earned by the individual", 
                          "name": "Salary"
                        }], 
            "providerType": "Arrow"
          }, 
          separator = "|"
        ), 
        filePath = {
          "type": "concat_operation", 
          "properties": {
            "elements": [{
                            "type": "literal", 
                            "properties": {
                              "value": "/datasets/orchestration_datasets/csv/valid/csv_pipe_separator.csv"
                            }
                          }]
          }
        }
    )
    parent_pipeline__Reformat_1 = Task(
        task_id = "parent_pipeline__Reformat_1", 
        component = "Model", 
        modelName = "parent_pipeline__Reformat_1"
    )
    T_fsi_2022_download_xlsx_1 = Task(
        task_id = "T_fsi_2022_download_xlsx_1", 
        component = "OrchestrationTarget", 
        kind = "S3Target", 
        connector = Connection(kind = "s3", id = "s3"), 
        format = {
          "category": "file", 
          "kind": "xlsx", 
          "properties": {"header" : True, "ignoreCellFormatting" : True, "sheetName" : "Sheet1"}
        }, 
        properties = {
          "filePath": {
            "type": "concat_operation", 
            "properties": {
              "elements": [{
                              "type": "literal", 
                              "properties": {
                                "value": "/datasets/orchestration_datasets/xlsx/target/fsi-2022-download.xlsx"
                              }
                            }]
            }
          }
        }
    )
    file_example_XLSX_5000_1 = Task(
        task_id = "file_example_XLSX_5000_1", 
        component = "Dataset", 
        label = "file_example_XLSX_5000_1", 
        table = {
          "name": "{{ prophecy_tmp_source('parent_pipeline', 'file_example_XLSX_5000_1') }}", 
          "sourceType": "UnreferencedSource"
        }
    )
    all_type_table_1 = SourceTask(
        task_id = "all_type_table_1", 
        component = "OrchestrationSource", 
        kind = "MSSQLSource", 
        connector = Connection(kind = "mssql", id = "mssql"), 
        format = MSSQLFormat(
          schema = {
            "fields": [{"dataType" : {"type" : "binary"}, "name" : "ID"},                         {"dataType" : {"type" : "int32"}, "name" : "IntCol"},                         {"dataType" : {"type" : "int16"}, "name" : "SmallIntCol"},                         {"dataType" : {"type" : "uint8"}, "name" : "TinyIntCol"},                         {"dataType" : {"type" : "int64"}, "name" : "BigIntCol"},                         {"dataType" : {"type" : "float64"}, "name" : "DecimalCol"},                         {"dataType" : {"type" : "float64"}, "name" : "NumericCol"},                         {"dataType" : {"type" : "float64"}, "name" : "FloatCol"},                         {"dataType" : {"type" : "float64"}, "name" : "RealCol"},                         {"dataType" : {"type" : "float64"}, "name" : "MoneyCol"},                         {"dataType" : {"type" : "float64"}, "name" : "SmallMoneyCol"},                         {"dataType" : {"type" : "bool"}, "name" : "BitCol"},                         {"dataType" : {"type" : "utf8"}, "name" : "CharCol"},                         {"dataType" : {"type" : "utf8"}, "name" : "VarCharCol"},                         {"dataType" : {"type" : "utf8"}, "name" : "NCharCol"},                         {"dataType" : {"type" : "utf8"}, "name" : "NVarCharCol"},                         {"dataType" : {"type" : "utf8"}, "name" : "TextCol"},                         {"dataType" : {"type" : "utf8"}, "name" : "NTextCol"},                         {"dataType" : {"type" : "timestamp"}, "name" : "DateCol"},                         {"dataType" : {"type" : "timestamp"}, "name" : "TimeCol"},                         {"dataType" : {"type" : "timestamp"}, "name" : "DateTimeCol"},                         {"dataType" : {"type" : "timestamp"}, "name" : "SmallDateTimeCol"},                         {"dataType" : {"type" : "timestamp"}, "name" : "DateTime2Col"},                         {"dataType" : {"type" : "timestamp"}, "name" : "DateTimeOffsetCol"},                         {"dataType" : {"type" : "timestamp"}, "name" : "CreatedAt"}], 
            "providerType": "arrow"
          }
        ), 
        tableFullName = {"database" : "qa_performance", "name" : "all_type_table", "schema" : "qa_schema"}
    )
    mongo_deepNestedData_1 = Task(
        task_id = "mongo_deepNestedData_1", 
        component = "Dataset", 
        label = "mongo_deepNestedData_1", 
        table = {
          "name": "{{ prophecy_tmp_source('parent_pipeline', 'mongo_deepNestedData_1') }}", 
          "sourceType": "UnreferencedSource"
        }
    )
    file_example_XLSX_5000_1 = SourceTask(
        task_id = "file_example_XLSX_5000_1", 
        component = "OrchestrationSource", 
        kind = "SmartsheetSource", 
        connector = Connection(kind = "smartsheet", id = "smartsheet"), 
        format = SMARTSHEETFormat(
          additionalProperties = {"copilot" : {"datasetDescriptionStatus" : "fromCopilot"}}, 
          description = "Demographic data capturing personal details and age, useful for understanding customer profiles.", 
          ignoreCellFormatting = True, 
          schema = {
            "fields": [{
                          "dataType": {"type" : "int64"}, 
                          "description": "A unique identifier for each record", 
                          "name": "Column1"
                        },                         {
                          "dataType": {"type" : "utf8"}, 
                          "description": "The first name of the individual", 
                          "name": "First Name"
                        },                         {
                          "dataType": {"type" : "utf8"}, 
                          "description": "The surname of the individual", 
                          "name": "Last Name"
                        },                         {"dataType" : {"type" : "utf8"}, "description" : "The gender of the individual", "name" : "Gender"},                         {
                          "dataType": {"type" : "utf8"}, 
                          "description": "The country where the individual resides", 
                          "name": "Country"
                        },                         {"dataType" : {"type" : "int64"}, "description" : "The age of the individual", "name" : "Age"},                         {
                          "dataType": {"type" : "utf8"}, 
                          "description": "The date associated with the record as a string", 
                          "name": "Date"
                        },                         {
                          "dataType": {"type" : "int64"}, 
                          "description": "The unique identifier for each record", 
                          "name": "Id"
                        }], 
            "providerType": "Arrow"
          }
        ), 
        filePath = "/QA Project/file_example_XLSX_5000"
    )
    parent_pipeline__Reformat_4 = Task(
        task_id = "parent_pipeline__Reformat_4", 
        component = "Model", 
        modelName = "parent_pipeline__Reformat_4"
    )
    fsi_2022_download_xlsx_1 = SourceTask(
        task_id = "fsi_2022_download_xlsx_1", 
        component = "OrchestrationSource", 
        kind = "S3Source", 
        connector = Connection(kind = "s3", id = "s3"), 
        format = XLSXFormat(
          allowUndefinedRows = True, 
          ignoreCellFormatting = True, 
          schema = {
            "fields": [{"dataType" : {"type" : "utf8"}, "name" : "Country"},                         {"dataType" : {"type" : "date32"}, "name" : "Year"},                         {"dataType" : {"type" : "utf8"}, "name" : "Rank"},                         {"dataType" : {"type" : "float64"}, "name" : "Total"},                         {"dataType" : {"type" : "float64"}, "name" : "C1: Security Apparatus"},                         {"dataType" : {"type" : "float64"}, "name" : "C2: Factionalized Elites"},                         {"dataType" : {"type" : "float64"}, "name" : "C3: Group Grievance"},                         {"dataType" : {"type" : "float64"}, "name" : "E1: Economy"},                         {"dataType" : {"type" : "float64"}, "name" : "E2: Economic Inequality"},                         {"dataType" : {"type" : "float64"}, "name" : "E3: Human Flight and Brain Drain"},                         {"dataType" : {"type" : "float64"}, "name" : "P1: State Legitimacy"},                         {"dataType" : {"type" : "float64"}, "name" : "P2: Public Services"},                         {"dataType" : {"type" : "float64"}, "name" : "P3: Human Rights"},                         {"dataType" : {"type" : "float64"}, "name" : "S1: Demographic Pressures"},                         {"dataType" : {"type" : "float64"}, "name" : "S2: Refugees and IDPs"},                         {"dataType" : {"type" : "float64"}, "name" : "X1: External Intervention"}], 
            "providerType": "arrow"
          }, 
          allowIncompleteRows = True, 
          header = True
        ), 
        filePath = "/datasets/orchestration_datasets/xlsx/valid/fsi-2022-download.xlsx"
    )
    parent_pipeline__Limit_2 = Task(
        task_id = "parent_pipeline__Limit_2", 
        component = "Model", 
        modelName = "parent_pipeline__Limit_2"
    )
    all_type_non_partitioned_different_rows_1 = SourceTask(
        task_id = "all_type_non_partitioned_different_rows_1", 
        component = "OrchestrationSource", 
        kind = "DatabricksSource", 
        connector = Connection(kind = "databricks", authType = "pat", id = "dev_sql_databricks"), 
        format = DATABRICKSFormat(
          schema = {
            "fields": [{"dataType" : {"type" : "int8"}, "name" : "c_tinyint"},                         {"dataType" : {"type" : "int16"}, "name" : "c_smallint"},                         {"dataType" : {"type" : "int32"}, "name" : "c_int"},                         {"dataType" : {"type" : "int64"}, "name" : "c_bigint"},                         {"dataType" : {"type" : "float32"}, "name" : "c_float"},                         {"dataType" : {"type" : "float64"}, "name" : "c_double"},                         {"dataType" : {"type" : "utf8"}, "name" : "c_string"},                         {"dataType" : {"type" : "bool"}, "name" : "c_boolean"},                         {"dataType" : {"dataType" : {"type" : "utf8"}, "type" : "Array"}, "name" : "c_array"},                         {
                          "dataType": {
                            "fields": [{"dataType" : {"type" : "utf8"}, "name" : "city"},                                         {"dataType" : {"type" : "utf8"}, "name" : "state"},                                         {"dataType" : {"type" : "int64"}, "name" : "pin"}], 
                            "type": "Struct"
                          }, 
                          "name": "c_struct"
                        }], 
            "providerType": "arrow"
          }
        ), 
        tableFullName = {"database" : "qa_team", "name" : "all_type_non_partitioned_different_rows", "schema" : "qa_database"}
    )
    basic_seed = Task(
        task_id = "basic_seed", 
        component = "Dataset", 
        table = {"name" : "basic_seed", "sourceType" : "Seed"}
    )
    parent_pipeline__Reformat_5 = Task(
        task_id = "parent_pipeline__Reformat_5", 
        component = "Model", 
        modelName = "parent_pipeline__Reformat_5"
    )
    T_all_type_json_json_1 = Task(
        task_id = "T_all_type_json_json_1", 
        component = "OrchestrationTarget", 
        kind = "SharepointTarget", 
        connector = Connection(kind = "sharepoint", id = "sharepoint"), 
        format = {"category" : "file", "kind" : "json", "properties" : {}}, 
        properties = {
          "filePath": {
            "type": "concat_operation", 
            "properties": {
              "elements": [{
                              "type": "literal", 
                              "properties": {
                                "value": "/qa_datasets/orchestration_datasets/json/dict/target/all_type_json.json"
                              }
                            }]
            }
          }
        }
    )
    (
        parent_pipeline__Reformat_1.out_0
        >> [parent_pipeline__customer_data_with_details.in_2, parent_pipeline__customer_data_with_details.in_0,
              parent_pipeline__customer_data_with_details.in_4,
              parent_pipeline__customer_data_with_details.in_1,
              parent_pipeline__customer_data_with_details.in_3]
    )
    file_example_XLSX_5000_1.output_port_10 >> parent_pipeline__Limit_2.in_9
    mongo_deepNestedData_1.output_port_8 >> parent_pipeline__Limit_2.in_7
    all_type_non_partitioned_different_rows_1.output_port_3 >> parent_pipeline__Limit_2.in_4
    all_type_json_json_1.output_port_9 >> parent_pipeline__Limit_2.in_8
    (
        S9MB_annual_enterprise_survey_2023_financial_year_provisional_csv_1.out0
        >> [T_S9MB_annual_enterprise_survey_2023_financial_year_provisional_csv_1.in0,
              S9MB_annual_enterprise_survey_2023_financial_year_provisional_csv_1.input_port_4]
    )
    parent_pipeline__Reformat_3.out_0 >> T_ALL_TYPE_TABLE_2.in0
    basic_seed.out >> parent_pipeline__customer_data_with_details.in_3
    s3_employee_details_csv.output_port_5 >> parent_pipeline__customer_data_with_details.in_4
    all_type_table_1.output_port_11 >> parent_pipeline__Limit_2.in_10
    fsi_2022_download_xlsx_1.out0 >> [T_fsi_2022_download_xlsx_1.in0, fsi_2022_download_xlsx_1.input_port_2]
    ALL_TYPE_TABLE_2.output_port_0 >> [parent_pipeline__Limit_2.in_11, parent_pipeline__Reformat_3.in_0]
    mongo_deepNestedData_1.out0 >> [T_mongo_deepNestedData_1.in0, mongo_deepNestedData_1.input_port_8]
    fsi_2022_download_xlsx_1.output_port_2 >> parent_pipeline__Limit_2.in_3
    all_type_json_json_1.out0 >> [T_all_type_json_json_1.in0, all_type_json_json_1.input_port_9]
    file_example_XLSX_5000_1.out0 >> [T_file_example_XLSX_5000_1.in0, file_example_XLSX_5000_1.input_port_10]
    (
        parent_pipeline__customer_data_with_details.out_0
        >> [parent_pipeline__Limit_2.in_8, parent_pipeline__Reformat_5.in_0, parent_pipeline__Limit_2.in_9,
              parent_pipeline__Limit_2.in_2, parent_pipeline__Limit_2.in_5, parent_pipeline__Limit_2.in_6,
              parent_pipeline__Reformat_4.in_0, parent_pipeline__Limit_2.in_11,
              parent_pipeline__Limit_2.in_7, parent_pipeline__Limit_2.in_1, parent_pipeline__Limit_2.in_0,
              parent_pipeline__Limit_2.in_4, parent_pipeline__Limit_2.in_10, parent_pipeline__Limit_2.in_3]
    )
    all_type_non_partitioned_different_rows_1.out0 >> all_type_non_partitioned_different_rows_1.input_port_3
    S9MB_annual_enterprise_survey_2023_financial_year_provisional_csv_1.output_port_4 >> parent_pipeline__Limit_2.in_5
    s3_employee_details_csv.out0 >> [T_s3_target.in0, s3_employee_details_csv.input_port_5]
    all_type_table_1.out0 >> [T_all_type_table_1.in0, all_type_table_1.input_port_11]
    ALL_TYPE_TABLE_2.out0 >> ALL_TYPE_TABLE_2.input_port_0
