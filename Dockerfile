FROM apache/airflow:2.9.2-python3.11

COPY requirements.txt .

USER root
RUN apt-get update && \
    apt-get install -y gcc python3-dev wget gnupg procps && \
    wget -qO - https://packages.adoptium.net/artifactory/api/gpg/key/public | apt-key add - && \
    echo "deb [arch=amd64] https://packages.adoptium.net/artifactory/deb focal main" | tee /etc/apt/sources.list.d/adoptium.list && \
    apt-get update && \
    apt-get install -y temurin-11-jdk && \
    apt-get clean

ENV JAVA_HOME /usr/lib/jvm/temurin-11-jdk-amd64

# Ensure that ps command is executable by all users
RUN chmod +x /bin/ps

USER airflow

RUN pip install -r requirements.txt
