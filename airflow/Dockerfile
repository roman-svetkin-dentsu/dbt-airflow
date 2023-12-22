FROM apache/airflow:latest

USER root

# Install required system dependencies
# RUN apt-get update \
#     && apt-get install -y --no-install-recommends \
#         build-essential \
#         libpq-dev \
#     && apt-get clean \
#     && rm -rf /var/lib/apt/lists/*

USER airflow

# Install the required Python packages as airflow user
RUN pip install --no-cache-dir dbt-core dbt-postgres
