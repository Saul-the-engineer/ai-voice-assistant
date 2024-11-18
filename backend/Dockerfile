# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Install awscli for Fargate
RUN apt-get update && apt-get install -y awscli

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Expose the port that FastAPI runs on
EXPOSE 8000

# Set the PYTHONPATH environment variable to include the directory where your code is located
ENV PYTHONPATH=/app/src

# Run the FastAPI application with Uvicorn
CMD ["uvicorn", "app.main:create_app", "--factory", "--host", "0.0.0.0", "--port", "8000"]
