## Scripts to copy:

#### Dockerfile
- In your root docker-intro folder
# Dockerfile
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /docker-intro

# Copy local files into the container
COPY src/ ./src

# Copy requirements file and install dependencies
COPY requirements.txt /docker-intro/
RUN pip install --no-cache-dir -r requirements.txt

# Set the default command to run the Python script directly
CMD ["python", "/docker-intro/dijkstras.py"]