#!/bin/bash
set -e
set -o pipefail
#build the docker image
docker build -t python-flask-api:1 .

#install the helm chart
cd helm-chart
helm upgrade --install python-flask-api .

#add entry in /etc/hosts if not exists
grep -qxF '127.0.0.1 api-example.local' /etc/hosts || echo '127.0.0.1 api-example.local' | sudo tee -a /etc/hosts


