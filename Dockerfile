# syntax=docker/dockerfile:1

# Use the official Python image as base
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY ./app/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the content of the local app directory to the working directory
COPY ./app .

# Expose the Flask port
EXPOSE 5000

# Command to run the Flask API server
CMD ["python", "api.py"]