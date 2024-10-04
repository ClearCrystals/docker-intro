# Dockerfile
FROM python:3.12-slim

# set the working directory inside the container
WORKDIR /docker-intro

# dockerfile
FROM python:3.12-slim

# set the working directory inside the container
WORKDIR /docker-intro

# copy the pyproject.toml, setup.py, and requirements.txt into the container
COPY pyproject.toml requirements.txt /docker-intro/

# install pip and dependencies
RUN pip install --no-cache-dir -r requirements.txt

# copy the rest of the application code into the container
COPY . /docker-intro/

# install the package (this will expose the 'docker_intro' command)
RUN pip install -e .

# define the default command as the 'docker_intro' script
CMD ["docker_intro"]
