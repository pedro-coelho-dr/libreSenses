# Use the official Python image that's based on Debian and is relatively small in size
FROM python:3.10-slim

# Set environment variables that ensure output from python is sent straight to the terminal without buffering it first
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies required for Python packages like psycopg2
RUN apt-get update \
  && apt-get install -y libpq-dev gcc \
  && apt-get clean

# Set the working directory in the container
WORKDIR /app

# Copy the 'pyproject.toml' and 'poetry.lock' into the container
COPY pyproject.toml poetry.lock /app/

# Install poetry for Python package management
RUN pip install poetry

# Install the Python dependencies in '/app' directory
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

# Copy the rest of the app's code into the container
COPY . /app

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application using gunicorn as the WSGI server
CMD ["gunicorn", "project.wsgi:application", "--bind", "0.0.0.0:8000"]