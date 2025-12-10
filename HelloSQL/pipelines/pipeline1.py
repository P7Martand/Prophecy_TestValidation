Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)
SensorSchedule = SensorSchedule(enabled = False)

with DAG(Schedule = Schedule, SensorSchedule = SensorSchedule):
    customers_0 = Task(task_id = "customers_0", component = "Model", modelName = "customers")
    orders_1 = Task(task_id = "orders_1", component = "Model", modelName = "orders")
