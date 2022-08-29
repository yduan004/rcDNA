# Introduction
It is a web application that can be used to convert DNA sequence(s) into their reverse-complement counterpart.

# Run on Heroku
Go to https://rcdna.herokuapp.com/ to run this tool online.

# Run from Docker Hub
1. Install Docker on your machine by refering to [Get Docker](https://docs.docker.com/get-docker/)
2. The docker image of this application has been pushed to DockerHub, one can directly
build and run the application locally by running in shell the following commandline:
```sh
docker run yuzhu2/rcdna
```
Open http://localhost:1234 or http://0.0.0.0:1234 in your web browser to use the application.

# Run from local Docker
1. Git clone this repository to your local computer
```sh
git clone https://github.com/yduan004/rcDNA.git
```
2. Build and run docker images locally by running in shell the following commandlines:
```sh
cd rcDNA
docker build --tag rcdna .
docker run -p 1234:1234 rcdna
```
Open http://localhost:1234 or http://0.0.0.0:1234 in your web browser to use the application.