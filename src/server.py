from flows import kghub_example_task_flow
from prefect import serve

if __name__ == "__main__":

    kghub_example_task_deployment = kghub_example_task_flow.to_deployment(
        name="Clear name of your deployment",
        interval=60, # alternative: cron="5 4 * * *". Check crontab.guru to create the correct schedule expression
        parameters={"text": "Python is absolutely fabulous"}, # Input needs to be convertable to json
        description="Code found at: https://github.com/nens/prefect-kghub-example-task", # Place this in EACH deployment, so that it its clear which repo serves which deployment
        tags=["Your name", "Project keyword"] # Add the name of the first point of contact, and one or more keywords of the project
    )


    serve(kghub_example_task_deployment)  # It is possible to create multiple deployments and serve them all.
