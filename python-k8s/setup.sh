#!/bin/bash
set -e
set -o pipefail
#build the docker image
docker build -t python-flask-api:1 .

#install the helm chart
cd helm-chart
helm upgrade --install python-flask-api .
