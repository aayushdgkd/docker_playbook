# Helm Charts

1. Helm has been used to package the manifests that need to be deployed on kubernetes.
2. It makes handling of variables very easy using the values.yaml file
3. New revisions of the service can be easily deployed by changing the image tag in values.yaml

# Scaling
We can scale the application to multiple replicas and requests will be equally distributed between them
```sh
% kubectl scale deploy python-flask-api --replicas=4 
deployment.apps/python-flask-api scaled
% kubectl get po
NAME                                READY   STATUS    RESTARTS   AGE
python-flask-api-58dc7d9bd6-8jkhf   1/1     Running   0          71s
python-flask-api-58dc7d9bd6-qjc2b   1/1     Running   0          18m
python-flask-api-58dc7d9bd6-rcngg   1/1     Running   0          71s
python-flask-api-58dc7d9bd6-rhm6t   1/1     Running   0          71s

% curl http://api-example.local/api
{"hostname":"python-flask-api-58dc7d9bd6-rcngg","timestamp":"Fri, 04 Nov 2022 21:38:21 GMT"}
% curl http://api-example.local/api
{"hostname":"python-flask-api-58dc7d9bd6-qjc2b","timestamp":"Fri, 04 Nov 2022 21:38:27 GMT"}
% curl http://api-example.local/api
{"hostname":"python-flask-api-58dc7d9bd6-rhm6t","timestamp":"Fri, 04 Nov 2022 21:38:34 GMT"}
curl http://api-example.local/api
{"hostname":"python-flask-api-58dc7d9bd6-8jkhf","timestamp":"Fri, 04 Nov 2022 21:38:41 GMT"}
% curl http://api-example.local/api
{"hostname":"python-flask-api-58dc7d9bd6-rcngg","timestamp":"Fri, 04 Nov 2022 21:38:50 GMT"}

```

As we can see Requests are being routed to all replicas as per round robin algorithm
