from prefect import task, get_run_logger
import requests
import pandas as pd
from datetime import datetime
import json

# Constants
uuid_gpm_ts = "fb384ac4-c8e8-452e-83d3-30f23c522577"
uuid_gpm_rast = "f23e174e-0636-45f1-86fd-e543a7aa49ac"

lizard_api = 'https://weact.lizard.net/api/v4'
kghub_api = 'http://kghub.caiag.kg/api'


lizard_headers = {
    "username": "__key__",
    "password": "yLMMChiw.5inIEGlTVGsebmhAEQWSyFjoTVXsm2ln",
    "Content-Type": "application/json",
}



bearer_token = 'testing'

kghub_headers = {
    'Authorization': f'Bearer {bearer_token}',
    'Content-Type': 'application/json'  # Specify that the data is in JSON format
}

@task(retries=2)
def get_precipitation(uuid, start, end, coordinates):
    logger = get_run_logger()
    url = f"{lizard_api}/rasters/{uuid}/point/"
    lat = coordinates[0]
    lon = coordinates[1]
    params = {"geom": 'POINT (74.590958 42.871773)',
              "start": start.isoformat() + "Z",
              "stop": end.isoformat() + "Z"}

    r = requests.get(url, params=params, headers=lizard_headers)
    r.raise_for_status()
    df = pd.DataFrame(r.json()["results"])
    if df.empty:
        logger.error("No data retrieved")
    else:
        logger.info(f"Retrieved {len(df)} data points")
    return df


def post_timeseries(ts_uuid, df_data, json_headers):
    events_url = f"{kghub_api}/timeseries/{ts_uuid}/events/"
    events = df_data[['time', 'value']].to_dict(orient='records')
    print((events))
    print(json_headers)
    # POST each event to the server
    response = requests.post(
        url=events_url,
        data=json.dumps(events),
        headers=json_headers
    )

    return response.json()


start = datetime(2024,11,1,0,0,0)
end =  datetime(2024,11,6,0,0,0)
coordinates = (74.590958, 42.871773, 0.0)

df = get_precipitation(uuid_gpm_rast, start, end, coordinates)
post_timeseries(uuid_gpm_ts, df, kghub_headers)
