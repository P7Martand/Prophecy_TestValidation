with DAG():
    raw_customers = Task(
        task_id = "raw_customers", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "raw_customers", "sourceType" : "Seed", "alias" : ""}
    )
    pipeline1__user_order_aggregate = Task(
        task_id = "pipeline1__user_order_aggregate", 
        component = "Model", 
        modelName = "pipeline1__user_order_aggregate"
    )
    raw_orders = Task(
        task_id = "raw_orders", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "raw_orders", "sourceType" : "Seed", "alias" : ""}
    )
    raw_orders.out >> pipeline1__user_order_aggregate.in_0
    raw_customers.out >> pipeline1__user_order_aggregate.in_1
