# Monitoring

## Tech Stack/Libraries used

1. Prometheus
2. nginx-ingress with prometheus scraping enabled
3. Grafana

## Explanation

1. As all traffic to our service/app comes via the nginx-ingress, we can make use of the metrics exposed by it to monitor the health
2. We can monitor the traffic by checking the non 200 status codes and visualise the same on Grafana
3. Link to import json for the official dashboard - https://github.com/kubernetes/ingress-nginx/blob/main/deploy/grafana/dashboards/nginx.json

Prometheus Metrics Scrape URL for nginx ingress (localhost:10254/metrics) -
```sh
% kubectl get po -n ingress-nginx
NAME                                        READY   STATUS      RESTARTS   AGE
ingress-nginx-admission-create-fgmq7        0/1     Completed   0          4h21m
ingress-nginx-admission-patch-97985         0/1     Completed   1          4h21m
ingress-nginx-controller-5959f988fd-wlc56   1/1     Running     0          4h21m
% kubectl exec -it ingress-nginx-controller-5959f988fd-wlc56 -n ingress-nginx sh
kubectl exec [POD] [COMMAND] is DEPRECATED and will be removed in a future version. Use kubectl exec [POD] -- [COMMAND] instead.
/etc/nginx $ curl 127.0.0.1:10254/metrics |grep http
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 42601    0 42601    0     0  2069k      0 --:--:-- --:--:-- --:--:-- 2080k
nginx_ingress_controller_build_info{build="08848d69e0c83992c89da18e70ea708752f21d7a",controller_class="k8s.io/ingress-nginx",controller_namespace="ingress-nginx",controller_pod="ingress-nginx-controller-5959f988fd-wlc56",release="v1.2.1",repository="https://github.com/kubernetes/ingress-nginx"} 1
# HELP promhttp_metric_handler_requests_in_flight Current number of scrapes being served.
# TYPE promhttp_metric_handler_requests_in_flight gauge
promhttp_metric_handler_requests_in_flight 1
# HELP promhttp_metric_handler_requests_total Total number of scrapes by HTTP status code.
# TYPE promhttp_metric_handler_requests_total counter
promhttp_metric_handler_requests_total{code="200"} 3
promhttp_metric_handler_requests_total{code="500"} 0
promhttp_metric_handler_requests_total{code="503"} 0
```

An idea of how it will actually look -
![Dashboard](https://github.com/kubernetes/ingress-nginx/blob/main/deploy/grafana/dashboards/screenshot.png)

