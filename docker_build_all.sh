#!/bin/bash

docker build --pull --rm -f "Dockerfile_update_balance_sheet_statement" -t update_balance_sheet_statement:latest "."
docker build --pull --rm -f "Dockerfile_update_cash_flow_statement" -t update_cash_flow_statement:latest "."
docker build --pull --rm -f "Dockerfile_update_company_key_stats" -t update_company_key_stats:latest "."
docker build --pull --rm -f "Dockerfile_update_income_statement" -t update_income_statement:latest "."
docker build --pull --rm -f "Dockerfile_update_symbols_list" -t update_symbols_list:latest "."

docker-compose -f "docker-compose.yml" up -d --build --remove-orphans
