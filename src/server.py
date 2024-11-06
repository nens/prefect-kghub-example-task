from flows import kghub_example_task_flow
from prefect import serve

if __name__ == "__main__":
    kghub_example_task_deployment = kghub_example_task_flow.to_deployment(
        name="GPM data",
        # interval=60, # alternative: cron="5 4 * * *". Check crontab.guru to create the correct schedule expression
        description="Code found at: https://github.com/nens/prefect-kghub-example-task",  # Place this in EACH deployment, so that it its clear which repo serves which deployment
        tags=["KGhub", "example"],
    )

    serve(kghub_example_task_deployment)
