# Ensemble Analytics Timeline API Demo

## Set up
This project uses docker compose to run the containerised FastAPI.

Please ensure you have [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed.

Clone the repository, navigate to the folder in your terminal, and spin up the containter
```shell
docker compose up -d
```
_Note: this should also build the image._

## API
The container should now be running 
The API can be explored using the bundled docs by visiting,
```
localhost:8000/docs
```

You will find that there are only two endpoints:
```
localhost:8000/timeline/
localhost:8000/
```
The first will provide the static data necessary for the task.
The second is irrelevant.
