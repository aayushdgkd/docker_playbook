# Monitoring

## Tech Stack/Libraries used

1. Prometheus
2. nginx-ingress with prometheus scraping enabled
3. Grafana

## Explanation

1. As all traffic to our service/app comes via the nginx-ingress, we can make use of the metrics exposed by it to monitor the health
2. We can monitor the traffic by checking the non 200 status codes and visualise the same on Grafana
3. Link to import json for the official dashboard - https://github.com/kubernetes/ingress-nginx/blob/main/deploy/grafana/dashboards/nginx.json

An idea of how it will actually look -
![Dashboard](https://github.com/kubernetes/ingress-nginx/blob/main/deploy/grafana/dashboards/screenshot.png)

