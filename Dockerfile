# syntax=docker/dockerfile:1

FROM python:alpine

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
RUN ls
ENV username=45000
# Create a new user with UID 10016
RUN addgroup -g $username choreo && \
    adduser  --disabled-password  --no-create-home --uid $username --ingroup choreo choreouser
USER $username
EXPOSE 5000
CMD [ "flask", "run", "--host=0.0.0.0"]