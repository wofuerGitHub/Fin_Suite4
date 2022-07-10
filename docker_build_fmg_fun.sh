#!/bin/bash

docker build --pull --rm -f "Dockerfile_fmg_fun_balancesheet" -t fmg_fun_balancesheet:latest "."
docker build --pull --rm -f "Dockerfile_fmg_fun_cashflow" -t fmg_fun_cashflow:latest "."
docker build --pull --rm -f "Dockerfile_fmg_fun_income" -t fmg_fun_income:latest "."

docker-compose -f "docker-compose_fmg_fun.yml" up -d --build
