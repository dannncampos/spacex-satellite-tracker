# Spacex Satellite Tracking API

- Version: 1.0
- Author: Daniel Campos
- Date: 30/05/2022

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

## Description

Query attributes about SpaceX launches to determine the last known latitude/longitude of the satellite for a given time.

### Server Build

    docker-compose build && docker-compose up -d

### Testing Spacex Satellite Tracking API

After building the docker image and creating the container, access the address in your browser for Swagger documentations: http://127.0.0.1/docs and for Redoc documentations: http://127.0.0.1/redoc

### Load Tests

$ pytest {arquivo}