# Script to generate a base layer for the lambda function

# Remove container if it exists
docker rm layer-container

# build base layer
docker build -t base-layer .

# rename to layer-container
docker run --name layer-container base-layer

# Copy zip artifact to machine for CDK use
docker cp layer-container:layer.zip . && echo "Created layer.zip with updated base layer."