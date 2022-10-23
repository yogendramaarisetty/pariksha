# Python image to use.
FROM python:3.8.3-slim-buster

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2 \
    && pip install celery \
    && pip install django-celery-results \
    && pip install celery-progress
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


CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
