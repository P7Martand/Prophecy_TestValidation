with DAG():
    pipeline1__season_years = Task(
        task_id = "pipeline1__season_years", 
        component = "Model", 
        modelName = "pipeline1__season_years"
    )
