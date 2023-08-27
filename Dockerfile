# syntax=docker/dockerfile:1

FROM python:alpine

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
ENV DEMO_APP_USERNAME=10016
# Create a new user with UID 10016
RUN addgroup -g $DEMO_APP_USERNAME choreo && \
    adduser  --disabled-password  --no-create-home --uid $DEMO_APP_USERNAME --ingroup choreo choreouser
USER $username
EXPOSE 5000
CMD [ "flask", "run", "--host=0.0.0.0"]