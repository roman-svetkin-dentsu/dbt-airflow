#!/bin/bash
# (C) 2023 Dentsu London Ltd. All Rights Reserved.

# If the following command gives a "Unknown options: --no-include-email"
# error then the local version of AWSCLI needs to be upgraded
# http://docs.aws.amazon.com/cli/latest/userguide/awscli-install-bundle.html
# At time of writing `aws --version` returns `aws-cli/1.11.99` for me

VERSION=0.0.1

awsversion=$(aws --version | cut -d '/' -f 2 | cut -d '.' -f 1)

# Login to Amazon Elastic Container Registry
if [ "$awsversion" = "1" ]
then
    echo "awscli V1"
    eval $(aws ecr get-login --no-include-email --region eu-west-1)
elif [ "$awsversion" = "2" ]
then
    echo "awscli V2"
    aws ecr get-login-password --region eu-west-1 | docker login --password-stdin --username AWS https://777615138750.dkr.ecr.eu-west-1.amazonaws.com
else
    echo "Unknown AWS version above 2.x: $awsversion"
    exit
fi

# Push commands as advised by ECS 'View Push Commands' option on AWS ECS repository web site
docker buildx build --platform linux/amd64 --push -t 777615138750.dkr.ecr.eu-west-1.amazonaws.com/airflow_dbt:$VERSION .
