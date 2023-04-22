FROM ubuntu:20.04

ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/

RUN apt-get update -y \
&& apt-get install -y software-properties-common \
&& add-apt-repository ppa:deadsnakes/ppa \
&& apt-get install openjdk-8-jdk -y \
&& apt-get install python3-pip -y \
&& apt-get -y install libpq-dev gcc \
&& pip install psycopg2 \
&& pip install celery \
&& pip install django-celery-results \
&& pip install celery-progress \
&& export JAVA_HOME \
&& apt-get clean \
&& rm -rf /var/lib/apt/lists/*



# Set the working directory to /app
WORKDIR /app

# copy the requirements file used for dependencies
COPY requirements.txt .


# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

RUN pip freeze
# Install any needed packages specified in requirements.txt
#RUN pip install psycopg2-binary

# Copy the rest of the working directory contents into the container at /app
COPY . .

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8080"]
