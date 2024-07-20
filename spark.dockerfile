FROM bitnami/spark
RUN sudo apt-get update
RUN sudo apt-get install oracle-java8-installer
RUN curl https://jdbc.postgresql.org/download/postgresql-42.2.18.jar -o /opt/bitnami/spark/jars/postgresql-42.2.18.jar