with DAG():
    raw_orders = Task(
        task_id = "raw_orders", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "raw_orders", "sourceType" : "Seed", "alias" : ""}
    )
    raw_customers = Task(
        task_id = "raw_customers", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "raw_customers", "sourceType" : "Seed", "alias" : ""}
    )
    pipeline1__orders_customers_join = Task(
        task_id = "pipeline1__orders_customers_join", 
        component = "Model", 
        modelName = "pipeline1__orders_customers_join"
    )
    raw_orders.out >> pipeline1__orders_customers_join.in_0
    raw_customers.out >> pipeline1__orders_customers_join.in_1
