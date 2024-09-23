# docker-intro

This is a walkthrough into how to use docker as a base to start a project. 

[Link to the Presentation](https://docs.google.com/presentation/d/1zqfnOWnqOHjvUZkb0QuvHljSnHQIfNnT4HHIdox8Yx0/edit?usp=sharing)

## What is docker?

Docker is a tool that helps you create, manage, and run applications in a special, isolated environment called a container. Containers are like lightweight, portable, and self-contained shared host os kernal that have everything your application needs to run, such as the code, libraries, dependencies, and system tools, all packed together.

#### Different files within Repo and what do they do?

##### Dockerfile

- Is the instructions to build images.
- `docker build . -t name_of_docker_build`
- docker build here with the name(-t) of name_of_docker_build

- `docker run --rm -it --entrypoint bash name_of_docker_build`
- docker run remove after exit, iteractive entrypoint bash name_of_container

##### requirements.txt

- A list of packages you want to use in your project.

##### pyproject.toml

- Allows you to use the folder name to run the project.

#### Mounting your local directory
Don't have a dockerfile but wanna work in a container env.
`docker run --rm -it --entrypoint bash -v $PWD:/src python:3.12-slim`

