# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Install git
RUN apt-get update && \
    apt-get install -y git

# Install dbt
RUN pip install dbt-core

# Install dbt-postgres
RUN pip install dbt-postgres

# Set an environment variable to tell dbt where to find the profiles.yml file
ENV DBT_PROFILES_DIR=/root/.dbt/

# Set up a directory for your dbt project
WORKDIR /dbt_project

# Copy the entry point script into the container
COPY entrypoint.sh /entrypoint.sh

# Make the entrypoint.sh script executable
RUN chmod +x /entrypoint.sh

# Set the entrypoint script as the default command
ENTRYPOINT ["/entrypoint.sh"]
