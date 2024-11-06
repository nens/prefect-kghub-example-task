import json

import pandas as pd
import requests
from prefect import get_run_logger, task
from prefect.blocks.system import Secret

lizard_api = "https://weact.lizard.net/api/v4"
kghub_api = "http://kghub.caiag.kg/api"


@task(retries=2)
def get_precipitation(uuid, start, end, coordinates):
    lizard_api_key = Secret.load("lizard-api-key").get()

    lizard_headers = {
        "username": "__key__",
        "password": lizard_api_key,
        "Content-Type": "application/json",
    }

    logger = get_run_logger()
    url = f"{lizard_api}/rasters/{uuid}/point/"
    lat = coordinates[0]
    lon = coordinates[1]
    params = {
        "geom": f"POINT ({lat} {lon})",
        "start": start.isoformat() + "Z",
        "stop": end.isoformat() + "Z",
    }

    r = requests.get(url, params=params, headers=lizard_headers)
    r.raise_for_status()
    df = pd.DataFrame(r.json()["results"])
    if df.empty:
        logger.error("No data retrieved")
    else:
        logger.info(f"Retrieved {len(df)} data points")
    return df


@task(retries=2)
def post_timeseries(ts_uuid, df_data):
    kghub_token = Secret.load("kghub-token").get()

    kghub_headers = {
        "Authorization": f"Bearer {kghub_token}",
        "Content-Type": "application/json",  # Specify that the data is in JSON format
    }

    events_url = f"{kghub_api}/timeseries/{ts_uuid}/events/"
    events = df_data[["time", "value"]].to_dict(orient="records")

    # POST each event to the server
    response = requests.post(
        url=events_url, data=json.dumps(events), headers=kghub_headers
    )

    return response.json()
