from flows import kghub_example_task_flow
from prefect import serve

if __name__ == "__main__":
    kghub_example_task_deployment = kghub_example_task_flow.to_deployment(
        name="GPM data",
        cron="10 4 * * *",
        description="Code found at: https://github.com/nens/prefect-kghub-example-task",  # Place this in EACH deployment, so that it its clear which repo serves which deployment
        tags=["KGhub", "example"],
    )

    serve(kghub_example_task_deployment)
