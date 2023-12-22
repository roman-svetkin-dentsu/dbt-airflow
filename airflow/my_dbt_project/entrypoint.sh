#!/bin/bash

# Clone the dbt repository
git clone https://github.com/yourusername/yourdbtrepo.git /my_dbt_project

# Navigate into the project directory
cd /dbt_project

# Execute the command passed to the docker run command
exec "$@"
