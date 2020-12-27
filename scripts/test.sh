#! /usr/bin/env bash

# Exit in case of error
set -e

docker-compose down -v --remove-orphans # Remove possibly previous broken stacks left hanging after an error

docker-compose build
docker-compose up -d
#docker-compose exec api_app pytest .
docker-compose exec api_app pytest --cov=app --cov-report=html app/tests "${@}"
docker-compose down
