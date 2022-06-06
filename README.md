# Spacex Satellite Tracking API

- Version: 1.0
- Author: Daniel Campos
- Date: 30/05/2022

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

## Description

Query attributes about SpaceX launches to determine the last known latitude/longitude of the satellite for a given time and the closest satellite by a given time and position.

## Endpoints:

| Endpoint                                        | Description                                                                               |
| ----------------------------------------------- | ----------------------------------------------------------------------------------------- |
| Get satellite position                          | Last known satellite position by ID and time.                                             |
| Get closest satellite                           | The closest satellite by given time and position on a globe as latitude and longitude     |

## Server Build

    docker-compose build && docker-compose up -d

## Testing Spacex Satellite Tracking API

After building the docker image and creating the container, access the address in your browser.

- Swagger documentations: http://127.0.0.1/docs
- Redoc documentations: http://127.0.0.1/redoc

## Query to determine the last known latitude and longitude of the satellite for a given time

    SELECT *
    FROM startlink_historical_data
    WHERE satellite_id='<str satellite_id>' and spacetrack_creation_date<='<datetime given_time>'
    ORDER BY spacetrack_creation_date
    DESC
    LIMIT 1;