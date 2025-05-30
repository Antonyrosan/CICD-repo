#!/bin/bash

# Set container and image names
CONTAINER_NAME="webserver_container"
IMAGE_NAME="webserver"

# Check if the container is running
if docker ps -q --filter "name=$CONTAINER_NAME" | grep -q .; then
    echo "🛑 Stopping running container: $CONTAINER_NAME..."
    docker stop "$CONTAINER_NAME"

    echo "🗑️ Removing container: $CONTAINER_NAME..."
    docker rm "$CONTAINER_NAME"
else
    echo "✅ No running container found with name: $CONTAINER_NAME"
fi

# Check if the image exists
if docker images -q "$IMAGE_NAME" | grep -q .; then
    echo "🗑️ Removing image: $IMAGE_NAME..."
    docker rmi "$IMAGE_NAME"
else
    echo "✅ No image found with name: $IMAGE_NAME"
fi

echo "🚀 Cleanup complete!"
