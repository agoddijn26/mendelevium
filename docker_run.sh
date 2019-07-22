#!/usr/bin/env bash
set -e

echo "cleanup containers"
containers=$(docker ps -a -f "label=service=${PWD##*/}" -q)
if [ ! -z "$containers" ]; then
    docker rm -f ${containers}
fi

echo "run container"
IMAGE=mendelevium

docker run --rm -it \
    -p 5000:5000 \
    -e FLASK_ENV=development \
    -e FLASK_DEBUG=false \
    ${IMAGE}:latest
