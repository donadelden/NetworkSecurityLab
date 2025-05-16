# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install flask

# Install iptables
RUN apt-get update && apt-get install -y iptables && apt-get clean

# Expose port 80 for the web server
EXPOSE 8080

# Run the Python script when the container launches
CMD ["python", "webpage.py"]