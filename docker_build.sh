#!/usr/bin/env bash
set -e

echo "build image"
IMAGE=mendelevium
TAG=`git log --format="%H" -n 1 | cut -c1-6`

docker build -t ${IMAGE}:${TAG} \
             -t ${IMAGE}:latest .
