from datetime import datetime, timedelta

from prefect import flow, get_run_logger
from tasks import get_precipitation, post_timeseries

# Constants
uuid_gpm_ts = "fb384ac4-c8e8-452e-83d3-30f23c522577"
uuid_gpm_rast = "f23e174e-0636-45f1-86fd-e543a7aa49ac"

coordinates = (74.590958, 42.871773, 0.0)


@flow(
    name="Clear name of your flow",
    flow_run_name="kghub_example_task Flow run",
    description="Short description of what the flow does.",
    retries=0,  # If wanted, place your retries count here,
    retry_delay_seconds=10,
    log_prints=True,
)
def kghub_example_task_flow():
    logger = get_run_logger()

    logger.info("Downloading precipitation data from Dutch Lizard")

    end = datetime.now().replace(microsecond=0, second=0, minute=0)
    start = end - timedelta(days=3)
    df = get_precipitation(uuid_gpm_rast, start, end, coordinates)

    logger.info("Data downloaded, uploading to KGhub")

    post_timeseries(uuid_gpm_ts, df)


if __name__ == "__main__":
    print("Not serving flows, but running them locally for testing")
    kghub_example_task_flow()
