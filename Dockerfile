# Dockerfile
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /docker-intro

# Dockerfile
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /docker-intro

# Copy the pyproject.toml, setup.py, and requirements.txt into the container
COPY pyproject.toml requirements.txt /docker-intro/

# Install pip and dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . /docker-intro/

# Install the package (this will expose the 'docker_intro' command)
RUN pip install -e .

# Define the default command as the 'docker_intro' script
CMD ["docker_intro"]
