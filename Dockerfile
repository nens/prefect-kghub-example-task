FROM python:3.12.3-bookworm
WORKDIR /code
LABEL project_name="prefect-kghub-example-task"

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
CMD ["python", "src/server.py"]
