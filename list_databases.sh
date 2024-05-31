#!/bin/bash

CONTAINER_NAME="postgres_db"

echo "Listing all databases in the PostgreSQL container '$CONTAINER_NAME':"
docker exec -it $CONTAINER_NAME psql -U postgres -c "\l"
