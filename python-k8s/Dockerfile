FROM python:3.8-alpine

WORKDIR /usr/src/app

COPY python-code/ .

RUN apk update && apk upgrade && apk add --no-cache gcc musl-dev libc-dev libc6-compat linux-headers build-base git libffi-dev openssl-dev

RUN pip install --no-cache-dir -r requirements.txt


CMD [ "python", "./app.py" ]
