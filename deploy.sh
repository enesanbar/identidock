#!/bin/bash
set -e

echo "Starting identidock system"

docker run --detach --restart=always --name redis redis:3
docker run --detach --restart=always --name dnmonster amouat/dnmonster:1.0
docker run --detach --restart=always \
    --link dnmonster:dnmonster \
    --link redis:redis \
    --env ENV=PROD \
    --name identidock amouat/identidock:1.0

docker run --detach --restart=always \
    --link identidock:identidock \
    --publish 80:80 \
    --env NGINX_HOST=192.168.99.113 \
    --env NGINX_PROXT=http://identidock:9090 \
    --name nginx amouat:proxy:1.0

echo "Started"