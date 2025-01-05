# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the required dependencies
RUN pip install flask requests

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run the application
CMD ["python", "example1.py"]
