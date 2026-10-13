from prophecy_pipeline_sdk.graph import *
from prophecy_pipeline_sdk.properties import *
Schedules = [Schedule(
               Name = "Schedule 1",
               emails = ["email@gmail.com"],
               enabled = False,
               cron = "* 0 2 * * * *",
               timezone = "GMT"
             )]
args = PipelineArgs(label = "pipeline1", version = 1, auto_layout = False, schedules = Schedules)

with Pipeline(args) as pipeline:
    pipeline1__payment_details = Process(
        name = "pipeline1__payment_details",
        properties = ModelTransform(modelName = "pipeline1__payment_details"),
        input_ports = ["in_0", "in_1"]
    )
    raw_customers = Process(
        name = "raw_customers",
        properties = Dataset(
          writeOptions = {"writeMode" : "overwrite"},
          table = Dataset.DBTSource(name = "raw_customers", sourceType = "Seed")
        ),
        input_ports = None
    )
    raw_payments = Process(
        name = "raw_payments",
        properties = Dataset(
          writeOptions = {"writeMode" : "overwrite"},
          table = Dataset.DBTSource(name = "raw_payments", sourceType = "Seed")
        ),
        input_ports = None,
        comment = "Overwrites the raw payments dataset with new data."
    )
    raw_payments >> pipeline1__payment_details._in(0)
    raw_customers >> pipeline1__payment_details._in(1)
