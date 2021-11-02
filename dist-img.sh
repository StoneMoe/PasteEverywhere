#!/usr/bin/env sh

NAMESPACE=$1
VERSION=$2

echo "Building..."
docker-compose -f docker-compose.local.yml build

echo "Publishing $VERSION to https://hub.docker.com/u/$NAMESPACE"
docker tag p-web:local "$NAMESPACE"/p-web:"$VERSION"
docker tag p-api:local "$NAMESPACE"/p-api:"$VERSION"
docker push "$NAMESPACE"/p-web:"$VERSION"
docker push "$NAMESPACE"/p-api:"$VERSION"

echo "Updating default docker-compose.yml"
sed -i -n -E "s/p-web:(.+)/p-web:$VERSION/" docker-compose.yml
sed -i -n -E "s/p-api:(.+)/p-api:$VERSION/" docker-compose.yml

echo "All Done."
echo "Check docker-compose.yml changes before commit."
