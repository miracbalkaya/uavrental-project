# Use the official Python image as the base image
FROM python:3.9-slim

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Copy the Django project files into the container
COPY . /app/

# Collect static files
# RUN python manage.py collectstatic --noinput

# Run the Django application
CMD ["gunicorn", "uavrental.wsgi:application", "--bind", "0.0.0.0:8000"]

# Note: Adjust the CMD command based on your project's requirements.
