# Prefect-kghub-example-task prefect task

This is an example task on how to develop operational data flows for the KGhub, the WE-ACT datawarehouse in Kyrgyzstan.
This script uses the [KGhub worker](https://kghubworker.caiag.kg) to upload data to the [KGhub](https://kghub.caiag.kg/api).
Some other examples for which the KGhubworker can be used.
- Processing csv files from an ftp to load data ito the KGhub
- Downloading data from external API's into the KGhub.
- Calculating discharges from waterlevel measurements in real time.

## Project Documentation

This script downloads rainfall data for Bishkek from the Dutch Lizard and posts it to the KGhub as a timeseries.

The task runs every day at 04:10 GMT.

## Developing your own tasks

The KGhub worker uses Prefect[https://prefect.com] to operationally run Python scripts. If you have your own tasks that you want to run operationally in the KGhub worker you can set them up similarly to this repository.
At least the following files should be present.

- A **README.md** describing what the task does.
- A **src/flows.py** which contains the main script. Optionally the script can be split up in separate tasks which can be put in the **src.tasks.py**.
- A **src/server.py** to control the task run frequency and other setting. Copy it from the repo and adjust as needed.
- A **Dockerfile** to build the docker, copy it from this repository.
- A **docker-compose.yml**
- A **requirements.txt** showing which Python packages are used.

For more info see the Prefect [getting started](https://docs-2.prefect.io/latest/) page.
For any questions and to actually deploy your script, reach out to Martijn Krol (martijn.krol@nelen-schuurmans.nl) or Kizje Marif (kizje.marif@nelen-schuurmans.nl).
