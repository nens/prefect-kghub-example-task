from prefect import flow
from tasks import uppercase_the_text


@flow(
    name="Clear name of your flow",
    flow_run_name = "kghub_example_task Flow run",
    description= "Short description of what the flow does.",
    retries=0, # If wanted, place your retries count here,
    retry_delay_seconds=10,
    log_prints=True
)
def kghub_example_task_flow(text: str = "Hi"):
    uppercase_text = uppercase_the_text(text)
    print(f"Turned {text} into {uppercase_text}")


if __name__ == "__main__":
    print("Not serving flows, but running them locally for testing")
    kghub_example_task_flow()
