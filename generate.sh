#!/bin/sh

# This will get the full MD5 sum and keep the container running, mapping files to PWD
CONTAINER_MD5=`docker run -v $PWD:/code -d vanessa/thesis tail -f /dev/null`

# Take the first 12 characters
CONTAINER_ID=`echo ${CONTAINER_MD5} | cut -c1-12`

# Send the command to the container to run the python script
docker exec $CONTAINER_ID python /code/generate.py

# stop the container
echo "Stopping container..."
docker stop $CONTAINER_ID

echo "Thesis generation finished, look in site folder for output, and add index.html and site folder to github pages!"

