#!/bin/bash

docker build --pull --rm -f "Dockerfile_fmg_stream_fx" -t fmg_stream_fx:latest "."
docker build --pull --rm -f "Dockerfile_fmg_stream_quote" -t fmg_stream_quote:latest "."

docker-compose -f "docker-compose_fmg_stream.yml" up -d --build
