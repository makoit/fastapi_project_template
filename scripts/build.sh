#! /usr/bin/env sh

# Exit in case of error
set -e

TAG=${BUILD_TAG} \
docker-compose \
-f docker-compose.yml \
build
