#!/bin/bash

docker build --pull --rm -f "Dockerfile_fmg_analyze_pvs" -t fmg_analyze_pvs:latest "."
docker build --pull --rm -f "Dockerfile_fmg_analyze_correlation" -t fmg_analyze_correlation:latest "."
docker build --pull --rm -f "Dockerfile_fmg_analyze_optimization" -t fmg_analyze_optimization:latest "."

docker-compose -f "docker-compose_fmg_analyze.yml" up -d --build
