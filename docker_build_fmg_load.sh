#!/bin/bash

docker build --pull --rm -f "Dockerfile_fmg_load_fx" -t fmg_load_fx:latest "."
docker build --pull --rm -f "Dockerfile_fmg_load_quote" -t fmg_load_quote:latest "."

docker-compose -f "docker-compose_fmg_load.yml" up -d --build
