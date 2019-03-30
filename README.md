# Carmen

A simple websockets app for learning purposes.

Carmen is an app that displays a random country that is constantly changing.

Components:
- api: A make believe third party API. This is a REST endpoint that returns a random country (ISO 3166 format) that changes periodically.
- backend: Coming soon, a websockets service to poll the api and push the current country to consumers.
- frontend: Coming soon, a visual rendering of the current country, obtained via websockets
