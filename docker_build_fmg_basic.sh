#!/bin/bash

docker build --pull --rm -f "Dockerfile_fmg_basic_symbolslist" -t fmg_basic_symbolslist:latest "."
docker build --pull --rm -f "Dockerfile_fmg_basic_companykeystats" -t fmg_basic_companykeystats:latest "."

docker-compose -f "docker-compose_fmg_basic.yml" up -d --build
