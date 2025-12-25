#!/bin/bash
VERSION=$(date +%Y%m%d%H%M)
IMAGE_NAME="my-app"
REGISTRY="ghcr.io/tritmeri"

podman build -t $REGISTRY/$IMAGE_NAME:$VERSION .
podman tag $REGISTRY/$IMAGE_NAME:$VERSION $REGISTRY/$IMAGE_NAME:latest
podman push $REGISTRY/$IMAGE_NAME:$VERSION
podman push $REGISTRY/$IMAGE_NAME:latest
