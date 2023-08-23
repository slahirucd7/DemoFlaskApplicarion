# syntax=docker/dockerfile:1

FROM python:3.9.17
RUN /usr/local/bin/python -m pip install --upgrade pip

WORKDIR python-docker

RUN groupadd -g 10005 go \
&& useradd -m -u 10006 -g go go
USER 10006

COPY requirements.txt requirements.txt
COPY . .
EXPOSE 5000
RUN . venv/bin/activate
RUN echo "Listing the path"
RUN ls -al
RUN pip install -r requirements.txt
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]