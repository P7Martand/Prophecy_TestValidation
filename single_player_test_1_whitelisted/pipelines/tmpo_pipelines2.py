Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)
SensorSchedule = SensorSchedule(enabled = False)

with DAG(Schedule = Schedule, SensorSchedule = SensorSchedule):
    complex2_csv_1 = Task(
        task_id = "complex2_csv_1", 
        component = "Dataset", 
        label = "complex2_csv_1", 
        table = {"name" : "{{ prophecy_tmp_source('tmpo_pipelines2', 'complex2_csv_1') }}", "sourceType" : "UnreferencedSource"}
    )
    Script_1 = Task(
        task_id = "Script_1", 
        component = "Script", 
        ports = None, 
        scriptMethodHeader = "def Script(spark: SparkSession, in0: DataFrame) -> DataFrame:", 
        scriptMethodFooter = "return out0", 
        script = "print('Hello There !' + in0.FileName)
out0 = in0"
    )
    tmpo_pipelines2__person_details_joined = Task(
        task_id = "tmpo_pipelines2__person_details_joined", 
        component = "Model", 
        modelName = "tmpo_pipelines2__person_details_joined"
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
    tmpo_pipelines2__Reformat_3 = Task(
        task_id = "tmpo_pipelines2__Reformat_3", 
        component = "Model", 
        modelName = "tmpo_pipelines2__Reformat_3"
    )
    tmpo_pipelines2__Reformat_2 = Task(
        task_id = "tmpo_pipelines2__Reformat_2", 
        component = "Model", 
        modelName = "tmpo_pipelines2__Reformat_2"
    )
    tmpo_pipelines2__generate_unique_id_with_timestamp = Task(
        task_id = "tmpo_pipelines2__generate_unique_id_with_timestamp", 
        component = "Model", 
        modelName = "tmpo_pipelines2__generate_unique_id_with_timestamp"
    )
    Table_0 = Task(
        task_id = "Table_0", 
        component = "Dataset", 
        table = {"name" : "seedraw", "sourceType" : "Seed"}, 
        writeOptions = {"writeMode" : "overwrite"}
    )
    anything4_csv_1 = Task(
        task_id = "anything4_csv_1", 
        component = "Dataset", 
        label = "anything4_csv_1", 
        table = {"name" : "{{ prophecy_tmp_source('tmpo_pipelines2', 'anything4_csv_1') }}", "sourceType" : "UnreferencedSource"}
    )
    anything4_csv_1 = SourceTask(
        task_id = "anything4_csv_1", 
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
            "fields": [{"name" : "c_int", "dataType" : {"type" : "int64"}},                         {"name" : "FileName", "dataType" : {"type" : "utf8"}}]
          }, 
          header = True
        ), 
        fileOperationProperties = {"fileLoadingType" : "filepath", "includeFileNameColumn" : True}, 
        filePath = "/anything4.csv"
    )
    (
        Table_0.out
        >> [tmpo_pipelines2__generate_unique_id_with_timestamp.in_0, tmpo_pipelines2__person_details_joined.in_0,
              tmpo_pipelines2__person_details_joined.in_1]
    )
    complex2_csv_1.output_port_3 >> tmpo_pipelines2__Reformat_3.in_0
    anything4_csv_1.out0 >> [Script_1.in0, anything4_csv_1.input_port_1]
    complex2_csv_1.out0 >> complex2_csv_1.input_port_3
    anything4_csv_1.output_port_1 >> tmpo_pipelines2__Reformat_2.in_0
