Schedule = Schedule(cron = "0 41 17 * * ? *", timezone = "Asia/Kolkata")
SensorSchedule = SensorSchedule(enabled = False)

with DAG(Schedule = Schedule, SensorSchedule = SensorSchedule):
    checkxa3_csv_1 = Task(
        task_id = "checkxa3_csv_1", 
        component = "Dataset", 
        label = "checkxa3_csv_1", 
        table = {"name" : "{{ prophecy_tmp_source('tmp_pipelines', 'checkxa3_csv_1') }}", "sourceType" : "UnreferencedSource"}
    )
    tmp_pipelines__smarsheet2 = Task(
        task_id = "tmp_pipelines__smarsheet2", 
        component = "Model", 
        modelName = "tmp_pipelines__smarsheet2"
    )
    tmp_pipelines__checkxa3_data = Task(
        task_id = "tmp_pipelines__checkxa3_data", 
        component = "Model", 
        modelName = "tmp_pipelines__checkxa3_data"
    )
    testresults_csv_1 = Task(
        task_id = "testresults_csv_1", 
        component = "Dataset", 
        label = "testresults_csv_1", 
        table = {"name" : "{{ prophecy_tmp_source('tmp_pipelines', 'testresults_csv_1') }}", "sourceType" : "UnreferencedSource"}
    )
    Script_1 = Task(
        task_id = "Script_1", 
        component = "Script", 
        ports = None, 
        scriptMethodHeader = "def Script(spark: SparkSession, in0: DataFrame) -> DataFrame:", 
        scriptMethodFooter = "return out0", 
        script = "print('Hello, Passed till here !!')
out0 = in0"
    )
    tmp_pipelines__Limit_1 = Task(
        task_id = "tmp_pipelines__Limit_1", 
        component = "Model", 
        modelName = "tmp_pipelines__Limit_1"
    )
    tmp_pipelines__Reformat_2 = Task(
        task_id = "tmp_pipelines__Reformat_2", 
        component = "Model", 
        modelName = "tmp_pipelines__Reformat_2"
    )
    tmp_pipelines__Filter_1 = Task(
        task_id = "tmp_pipelines__Filter_1", 
        component = "Model", 
        modelName = "tmp_pipelines__Filter_1"
    )
    tmp_pipelines__Reformat_3 = Task(
        task_id = "tmp_pipelines__Reformat_3", 
        component = "Model", 
        modelName = "tmp_pipelines__Reformat_3"
    )
    tmp_pipelines__all_concatenated_dates = Task(
        task_id = "tmp_pipelines__all_concatenated_dates", 
        component = "Model", 
        modelName = "tmp_pipelines__all_concatenated_dates"
    )
    target_file_pr_1 = SourceTask(
        task_id = "target_file_pr_1", 
        component = "OrchestrationSource", 
        kind = "SmartsheetSource", 
        connector = Connection(kind = "smartsheet", id = "smartsheet_1"), 
        format = SMARTSHEETFormat(
          ignoreCellFormatting = True, 
          schema = {
            "providerType": "Arrow", 
            "fields": [{"name" : "Primary_Column", "dataType" : {"type" : "utf8"}},                         {"name" : "Assigned_To", "dataType" : {"type" : "utf8"}},                         {"name" : "Status", "dataType" : {"type" : "utf8"}},                         {"name" : "Start_Date", "dataType" : {"type" : "utf8"}},                         {"name" : "End_Date", "dataType" : {"type" : "utf8"}},                         {"name" : "Duration", "dataType" : {"type" : "utf8"}},                         {"name" : "At_Risk", "dataType" : {"type" : "utf8"}},                         {"name" : "Modified_By", "dataType" : {"type" : "utf8"}},                         {"name" : "Modification_Date", "dataType" : {"type" : "utf8"}},                         {"name" : "Column10", "dataType" : {"type" : "utf8"}},                         {"name" : "Column11", "dataType" : {"type" : "utf8"}},                         {"name" : "Column12", "dataType" : {"type" : "utf8"}},                         {"name" : "Column13", "dataType" : {"type" : "utf8"}},                         {"name" : "Column14", "dataType" : {"type" : "utf8"}},                         {"name" : "Column15", "dataType" : {"type" : "utf8"}},                         {"name" : "Column16", "dataType" : {"type" : "utf8"}},                         {"name" : "Column17", "dataType" : {"type" : "utf8"}},                         {"name" : "Column18", "dataType" : {"type" : "utf8"}},                         {"name" : "Column19", "dataType" : {"type" : "utf8"}},                         {"name" : "Column20", "dataType" : {"type" : "utf8"}},                         {"name" : "Column21", "dataType" : {"type" : "utf8"}},                         {"name" : "Column22", "dataType" : {"type" : "utf8"}},                         {"name" : "Column23", "dataType" : {"type" : "utf8"}}]
          }, 
          description = ""
        ), 
        filePath = "/newtarget/target_file_pr"
    )
    RestAPI_1 = Task(
        task_id = "RestAPI_1", 
        component = "RestAPI", 
        method = "GET", 
        body = "", 
        url = "https://mpe86b5de1c6d0ae1869.free.beeceptor.com/data", 
        targetColumnName = "Status", 
        params = [], 
        headers = []
    )
    complex2_csv_1 = Task(
        task_id = "complex2_csv_1", 
        component = "Dataset", 
        label = "complex2_csv_1", 
        table = {"name" : "{{ prophecy_tmp_source('tmp_pipelines', 'complex2_csv_1') }}", "sourceType" : "UnreferencedSource"}
    )
    tmp_pipelines__Reformat_4 = Task(
        task_id = "tmp_pipelines__Reformat_4", 
        component = "Model", 
        modelName = "tmp_pipelines__Reformat_4"
    )
    target_file_pr_1 = Task(
        task_id = "target_file_pr_1", 
        component = "Dataset", 
        label = "target_file_pr_1", 
        table = {"name" : "{{ prophecy_tmp_source('tmp_pipelines', 'target_file_pr_1') }}", "sourceType" : "UnreferencedSource"}
    )
    testresults_csv_1 = SourceTask(
        task_id = "testresults_csv_1", 
        component = "OrchestrationSource", 
        kind = "SharepointSource", 
        connector = Connection(kind = "sharepoint", id = "sharepoint_1"), 
        format = CSVFormat(
          allowLazyQuotes = False, 
          allowEmptyColumnNames = True, 
          description = "", 
          separator = ",", 
          nullValue = "", 
          encoding = "UTF-8", 
          schema = {
            "providerType": "Arrow", 
            "fields": [{"name" : "5524", "dataType" : {"type" : "int64"}},                         {"name" : "User_861", "dataType" : {"type" : "utf8"}},                         {"name" : "31", "dataType" : {"type" : "int64"}},                         {"name" : "112071.35", "dataType" : {"type" : "float64"}},                         {"name" : "true", "dataType" : {"type" : "bool"}},                         {"name" : "2000-08-14", "dataType" : {"type" : "date32"}},                         {"name" : "2023-11-23 21:11:09", "dataType" : {"type" : "timestamp"}},                         {"name" : "Green", "dataType" : {"type" : "utf8"}},                         {"name" : "96038.97", "dataType" : {"type" : "float64"}},                         {"name" : "false", "dataType" : {"type" : "bool"}},                         {"name" : "Swimming", "dataType" : {"type" : "utf8"}}]
          }, 
          header = True
        ), 
        filePath = "/test_target/arun/testresults.csv"
    )
    complex2_csv_1 = SourceTask(
        task_id = "complex2_csv_1", 
        component = "OrchestrationSource", 
        kind = "S3Source", 
        connector = Connection(kind = "s3", id = "s3_1"), 
        format = CSVFormat(
          allowLazyQuotes = False, 
          allowEmptyColumnNames = True, 
          description = "", 
          separator = ",", 
          nullValue = "", 
          encoding = "UTF-8", 
          schema = {
            "providerType": "Arrow", 
            "fields": [{"name" : "c_tinyint", "dataType" : {"type" : "int64"}},                         {"name" : "c_smallint", "dataType" : {"type" : "int64"}},                         {"name" : "c_int", "dataType" : {"type" : "int64"}},                         {"name" : "c_float", "dataType" : {"type" : "float64"}},                         {"name" : "c_double", "dataType" : {"type" : "float64"}},                         {"name" : "c_decimal", "dataType" : {"type" : "float64"}},                         {"name" : "c_boolean", "dataType" : {"type" : "bool"}},                         {"name" : "c_null", "dataType" : {"type" : "utf8"}},                         {"name" : "c_emptystring", "dataType" : {"type" : "utf8"}},                         {"name" : "c_date", "dataType" : {"type" : "date32"}},                         {"name" : "c_timestamp", "dataType" : {"type" : "timestamp"}},                         {"name" : "c_interval", "dataType" : {"type" : "utf8"}},                         {"name" : "c_time", "dataType" : {"type" : "utf8"}},                         {"name" : "c_array", "dataType" : {"type" : "utf8"}},                         {"name" : "c_struct", "dataType" : {"type" : "utf8"}},                         {"name" : "c_array_of_struct", "dataType" : {"type" : "utf8"}},                         {"name" : "c_struct_of_array", "dataType" : {"type" : "utf8"}},                         {"name" : "c_complex_struct", "dataType" : {"type" : "utf8"}},                         {"name" : "FileName", "dataType" : {"type" : "utf8"}}]
          }, 
          header = True
        ), 
        fileOperationProperties = {"fileLoadingType" : "filepath", "includeFileNameColumn" : True}, 
        filePath = "/complex2.csv"
    )
    DynamicInput_1 = Task(
        task_id = "DynamicInput_1", 
        component = "DynamicInput", 
        replaceSpecificString = [{"textToReplace" : "Almost Passed", "textToReplaceField" : "Status"}], 
        tableIntegration = "mssql", 
        tableConnector = Connection(kind = "mssql", id = "mssql_1"), 
        passFieldsToOutput = ["Primary_Column",  "Assigned_To",  "Status",  "Start_Date",  "End_Date",  "Duration",  "At_Risk",  "Modified_By",          "Modification_Date",  "Column10",  "Column11",  "Column12",  "Column13",  "Column14",  "Column15",  "Column16",          "Column17",  "Column18",  "Column19",  "Column20",  "Column21",  "Column22",  "Column23",  "Total_Date"], 
        sqlQuery = "select * from Script_1", 
        readOptions = "modifySQLQuery"
    )
    tmp_pipelines__person_details_joined = Task(
        task_id = "tmp_pipelines__person_details_joined", 
        component = "Model", 
        modelName = "tmp_pipelines__person_details_joined"
    )
    Table_0 = Task(
        task_id = "Table_0", 
        component = "Dataset", 
        table = {"name" : "seedraw", "sourceType" : "Seed"}, 
        writeOptions = {"writeMode" : "overwrite"}
    )
    OrchestrationTarget_1 = Task(
        task_id = "OrchestrationTarget_1", 
        component = "OrchestrationTarget", 
        kind = "SFTPTarget", 
        connector = Connection(kind = "sftp", id = "sftp_1"), 
        properties = {
          "filePath": {
            "type": "concat_operation", 
            "properties": {
              "elements": [{"type" : "literal", "properties" : {"value" : "/prophecy-sftp/prakhar/checkxa4.csv"}}]
            }
          }
        }, 
        format = {
          "properties": {
            "allowLazyQuotes": False, 
            "allowEmptyColumnNames": True, 
            "separator": ",", 
            "nullValue": "", 
            "encoding": "UTF-8", 
            "header": True
          }, 
          "kind": "csv", 
          "category": "file"
        }, 
        isNew = False
    )
    checkxa3_csv_1 = SourceTask(
        task_id = "checkxa3_csv_1", 
        component = "OrchestrationSource", 
        kind = "SFTPSource", 
        connector = Connection(kind = "sftp", authMethod = "password", id = "sftp_1", port = 22), 
        format = CSVFormat(
          allowLazyQuotes = False, 
          allowEmptyColumnNames = True, 
          description = "", 
          separator = ",", 
          nullValue = "", 
          encoding = "UTF-8", 
          schema = {
            "providerType": "Arrow", 
            "fields": [{"name" : "id", "dataType" : {"type" : "int64"}},                         {"name" : "name", "dataType" : {"type" : "utf8"}},                         {"name" : "updated_at", "dataType" : {"type" : "date32"}},                         {"name" : "FileName", "dataType" : {"type" : "utf8"}}]
          }, 
          header = True
        ), 
        fileOperationProperties = {"fileLoadingType" : "filepath", "includeFileNameColumn" : True}, 
        filePath = "/prophecy-sftp/prakhar/checkxa3.csv"
    )
    tmp_pipelines__Reformat_4.out_0 >> tmp_pipelines__smarsheet2.in_0
    complex2_csv_1.out0 >> complex2_csv_1.input_port_2
    Table_0.out >> [tmp_pipelines__person_details_joined.in_0, tmp_pipelines__person_details_joined.in_1]
    testresults_csv_1.out0 >> testresults_csv_1.input_port_5
    checkxa3_csv_1.out0 >> checkxa3_csv_1.input_port_0
    target_file_pr_1.out0 >> target_file_pr_1.input_port_6
    complex2_csv_1.output_port_2 >> tmp_pipelines__Reformat_3.in_0
    testresults_csv_1.output_port_5 >> tmp_pipelines__Reformat_4.in_0
    Script_1.out0 >> DynamicInput_1.in0
    (
        checkxa3_csv_1.output_port_0
        >> [tmp_pipelines__Limit_1.in_0, tmp_pipelines__checkxa3_data.in_0, tmp_pipelines__Filter_1.in_0,
              tmp_pipelines__Reformat_2.in_0]
    )
    tmp_pipelines__Reformat_2.out_0 >> OrchestrationTarget_1.in0
    tmp_pipelines__all_concatenated_dates.out_0 >> [Script_1.in0, RestAPI_1.in0]
    target_file_pr_1.output_port_6 >> tmp_pipelines__all_concatenated_dates.in_0
