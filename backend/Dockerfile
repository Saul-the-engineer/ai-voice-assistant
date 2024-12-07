# Run with the following command:
# docker build -t backend .

# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app/backend

# Install system dependencies
RUN apt-get update && apt-get install -y \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Copy the llama model into the container at /app/backend/models
COPY ./models /app/backend/models

# Copy the requirements file into the container at /app
COPY ./requirements.txt /app/backend

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY ./src /app/backend/src

# Expose the port that FastAPI runs on
EXPOSE 8000

# Set the PYTHONPATH environment variable to include the directory where your code is located
ENV PYTHONPATH=/app/backend/src

# Run the FastAPI application with Uvicorn
CMD ["uvicorn", "app.main:create_app", "--factory", "--host", "0.0.0.0", "--port", "8000"]

# To run the container, use the following command:
# docker run -p 8000:8000 --name AI-Voice-Assistent backend
