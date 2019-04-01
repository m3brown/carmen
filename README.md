# Carmen

A simple websockets app for learning purposes.

Carmen is an app that displays a random country that is constantly changing.

## Components

- api: A make believe third party API. This is a REST endpoint that returns a random country (ISO 3166 format) that changes periodically.
- backend: A websockets service to poll the api and push the current country to consumers.
- frontend: A visual rendering of the current country, obtained via websockets

## Setup

There are two ways to launch the service: manual and docker

### Docker

```shell
docker-compose up
# open http://localhost:8000 in your browser
```

### Manual setup

```shell
# setup
pip install pipenv plz-cmd  # requires python 3.6+ and pip to be installed
plz setup

# launch first app in one terminal
plz api

# launch second app in another terminal
plz backend

# open the frontend website in a third terminal
plz frontend
```
