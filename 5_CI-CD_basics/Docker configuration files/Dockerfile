FROM jenkins/jenkins:latest

USER root
RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y pip
RUN pip install pytest
RUN pip install pymssql

USER jenkins