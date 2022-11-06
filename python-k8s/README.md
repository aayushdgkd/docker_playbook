# Instructions to Deploy

## Prerequisites/Assumptions

1. docker is installed
2. kubectl is configured to connect to a cluster
3. system is compatible with bash scripts
4. helm is installed and connected to the cluster
5. system has internet access


## Steps to Build
1. Take the clone and get inside the python-k8s/ directory of the repo
2. Build your docker image -
```sh
docker build -t python-flask-api:1 .
```
3. Go to the "helm-chart" directory and update values.yaml with  repo:tag that you used in previous command. Defaults are already set to work as per document instructions
4. Install your helm chart
```sh
helm install python-flask-api .
```
5. Deployment,pod,Ingress and service will get created
6. Create entry in your "/etc/hosts" file - "127.0.0.1 api-example.local"
7. If you are feeling lucky,run "sh setup.sh" to setup everything at once. The output will look somewhat like this -

```sh
sh setup.sh
Sending build context to Docker daemon  25.09kB
Step 1/6 : FROM python:3.8-alpine
 ---> 6690c9c6e607
Step 2/6 : WORKDIR /usr/src/app
 ---> Using cache
 ---> 1cb509c95355
Step 3/6 : COPY python-code/ .
 ---> Using cache
 ---> 4608da8be60c
Step 4/6 : RUN apk update && apk upgrade && apk add --no-cache gcc musl-dev libc-dev libc6-compat linux-headers build-base git libffi-dev openssl-dev
 ---> Running in 38317306cf68
fetch https://dl-cdn.alpinelinux.org/alpine/v3.16/main/aarch64/APKINDEX.tar.gz
fetch https://dl-cdn.alpinelinux.org/alpine/v3.16/community/aarch64/APKINDEX.tar.gz
v3.16.2-424-g6c384a3497 [https://dl-cdn.alpinelinux.org/alpine/v3.16/main]
v3.16.2-422-gd4addd5b8e [https://dl-cdn.alpinelinux.org/alpine/v3.16/community]
OK: 16901 distinct packages available
(1/8) Upgrading musl (1.2.3-r0 -> 1.2.3-r1)
(2/8) Upgrading libcrypto1.1 (1.1.1q-r0 -> 1.1.1s-r0)
(3/8) Upgrading expat (2.4.9-r0 -> 2.5.0-r0)
(4/8) Upgrading libssl1.1 (1.1.1q-r0 -> 1.1.1s-r0)
(5/8) Upgrading alpine-baselayout-data (3.2.0-r22 -> 3.2.0-r23)
(6/8) Upgrading alpine-baselayout (3.2.0-r22 -> 3.2.0-r23)
Executing alpine-baselayout-3.2.0-r23.pre-upgrade
Executing alpine-baselayout-3.2.0-r23.post-upgrade
(7/8) Upgrading musl-utils (1.2.3-r0 -> 1.2.3-r1)
(8/8) Upgrading tzdata (2022c-r0 -> 2022f-r1)
Executing busybox-1.35.0-r17.trigger
Executing ca-certificates-20220614-r0.trigger
OK: 14 MiB in 36 packages
fetch https://dl-cdn.alpinelinux.org/alpine/v3.16/main/aarch64/APKINDEX.tar.gz
fetch https://dl-cdn.alpinelinux.org/alpine/v3.16/community/aarch64/APKINDEX.tar.gz
(1/29) Installing libgcc (11.2.1_git20220219-r2)
(2/29) Installing libstdc++ (11.2.1_git20220219-r2)
(3/29) Installing binutils (2.38-r3)
(4/29) Installing libmagic (5.41-r0)
(5/29) Installing file (5.41-r0)
(6/29) Installing libgomp (11.2.1_git20220219-r2)
(7/29) Installing libatomic (11.2.1_git20220219-r2)
(8/29) Installing gmp (6.2.1-r2)
(9/29) Installing isl22 (0.22-r0)
(10/29) Installing mpfr4 (4.1.0-r0)
(11/29) Installing mpc1 (1.2.1-r0)
(12/29) Installing gcc (11.2.1_git20220219-r2)
(13/29) Installing musl-dev (1.2.3-r1)
(14/29) Installing libc-dev (0.7.2-r3)
(15/29) Installing g++ (11.2.1_git20220219-r2)
(16/29) Installing make (4.3-r0)
(17/29) Installing fortify-headers (1.1-r1)
(18/29) Installing patch (2.7.6-r7)
(19/29) Installing build-base (0.5-r3)
(20/29) Installing brotli-libs (1.0.9-r6)
(21/29) Installing nghttp2-libs (1.47.0-r0)
(22/29) Installing libcurl (7.83.1-r4)
(23/29) Installing pcre2 (10.40-r0)
(24/29) Installing git (2.36.3-r0)
(25/29) Installing libc6-compat (1.2.3-r1)
(26/29) Installing linux-headers (5.16.7-r1)
(27/29) Installing pkgconf (1.8.0-r1)
(28/29) Installing libffi-dev (3.4.2-r1)
(29/29) Installing openssl-dev (1.1.1s-r0)
Executing busybox-1.35.0-r17.trigger
OK: 228 MiB in 65 packages
Removing intermediate container 38317306cf68
 ---> f1e7e3565feb
Step 5/6 : RUN pip install --no-cache-dir -r requirements.txt
 ---> Running in baa33d0bd426
Collecting flask==2.1.2
  Downloading Flask-2.1.2-py3-none-any.whl (95 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 95.2/95.2 KB 1.7 MB/s eta 0:00:00
Collecting itsdangerous>=2.0
  Downloading itsdangerous-2.1.2-py3-none-any.whl (15 kB)
Collecting Jinja2>=3.0
  Downloading Jinja2-3.1.2-py3-none-any.whl (133 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 133.1/133.1 KB 2.2 MB/s eta 0:00:00
Collecting importlib-metadata>=3.6.0
  Downloading importlib_metadata-5.0.0-py3-none-any.whl (21 kB)
Collecting Werkzeug>=2.0
  Downloading Werkzeug-2.2.2-py3-none-any.whl (232 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 232.7/232.7 KB 2.8 MB/s eta 0:00:00
Collecting click>=8.0
  Downloading click-8.1.3-py3-none-any.whl (96 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 96.6/96.6 KB 2.5 MB/s eta 0:00:00
Collecting zipp>=0.5
  Downloading zipp-3.10.0-py3-none-any.whl (6.2 kB)
Collecting MarkupSafe>=2.0
  Downloading MarkupSafe-2.1.1-cp38-cp38-musllinux_1_1_aarch64.whl (30 kB)
Installing collected packages: zipp, MarkupSafe, itsdangerous, click, Werkzeug, Jinja2, importlib-metadata, flask
Successfully installed Jinja2-3.1.2 MarkupSafe-2.1.1 Werkzeug-2.2.2 click-8.1.3 flask-2.1.2 importlib-metadata-5.0.0 itsdangerous-2.1.2 zipp-3.10.0
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
WARNING: You are using pip version 22.0.4; however, version 22.3.1 is available.
You should consider upgrading via the '/usr/local/bin/python -m pip install --upgrade pip' command.
Removing intermediate container baa33d0bd426
 ---> 9a4bbf720b3e
Step 6/6 : CMD [ "python", "./app.py" ]
 ---> Running in e140331ffceb
Removing intermediate container e140331ffceb
 ---> 1087a8e5047a
Successfully built 1087a8e5047a
Successfully tagged python-flask-api:1
Release "python-flask-api" does not exist. Installing it now.
NAME: python-flask-api
LAST DEPLOYED: Sun Nov  6 19:29:22 2022
NAMESPACE: default
STATUS: deployed
REVISION: 1
TEST SUITE: None
```
```sh
% kubectl get po,deploy,service,ing
NAME                                    READY   STATUS    RESTARTS   AGE
pod/python-flask-api-58dc7d9bd6-g5zpk   1/1     Running   0          30s

NAME                               READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/python-flask-api   1/1     1            1           30s

NAME                               TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)   AGE
service/kubernetes                 ClusterIP   10.96.0.1        <none>        443/TCP   124m
service/python-flask-api-service   ClusterIP   10.101.172.161   <none>        80/TCP    30s

NAME                                                 CLASS   HOSTS               ADDRESS   PORTS   AGE
ingress.networking.k8s.io/python-flask-api-ingress   nginx   api-example.local             80      30s
```

PS - This code is tested on a minikube cluster, to enable ingress controller on minikube you need to run - "minikube addons enable ingress" and "minikube tunnel"
