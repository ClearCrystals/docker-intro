# docker-intro

# Mounting your local directory (don't need docker)

`docker run --rm -it --entrypoint bash -v $PWD:/src python:3.12-slim`

# 
`docker build -t name_of_docker_build .`

docker run --rm -it -v $PWD/src:/docker-intro/src name_of_build

docker build -t name_of_docker_build . && docker run --rm -it --entrypoint bash name_of_docker_build