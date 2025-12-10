Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)
SensorSchedule = SensorSchedule(enabled = False)

with DAG(Schedule = Schedule, SensorSchedule = SensorSchedule):
    raw_payments = Task(
        task_id = "raw_payments", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "raw_payments", "sourceType" : "Seed"}
    )
    raw_orders = Task(
        task_id = "raw_orders", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "raw_orders", "sourceType" : "Seed", "alias" : ""}
    )
    pipeline1__payment_details = Task(
        task_id = "pipeline1__payment_details", 
        component = "Model", 
        modelName = "pipeline1__payment_details"
    )
    raw_payments.out >> pipeline1__payment_details.in_0
    raw_orders.out >> pipeline1__payment_details.in_1
