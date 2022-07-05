#!/bin/bash

docker build --pull --rm -f "Dockerfile_update_balance_sheet_statement" -t update_balance_sheet_statement:latest "."
docker build --pull --rm -f "Dockerfile_update_cash_flow_statement" -t update_cash_flow_statement:latest "."
docker build --pull --rm -f "Dockerfile_update_company_key_stats" -t update_company_key_stats:latest "."
docker build --pull --rm -f "Dockerfile_update_income_statement" -t update_income_statement:latest "."
docker build --pull --rm -f "Dockerfile_update_symbols_list" -t update_symbols_list:latest "."

docker build --pull --rm -f "Dockerfile_update_fx_eur" -t update_fx_eur:latest "."

docker build --pull --rm -f "Dockerfile_update_fx_stream" -t update_fx_stream:latest "."
docker build --pull --rm -f "Dockerfile_update_quote_stream" -t update_quote_stream:latest "."

docker build --pull --rm -f "Dockerfile_insert_quote" -t insert_quote:latest "."



docker-compose -f "docker-compose.yml" up -d --build

docker-compose -f "docker-compose_update_fx_eur.yml" up -d --build
docker-compose -f "docker-compose_insert_quote.yml" up -d --build

docker-compose -f "docker-compose_update_fx_stream.yml" up -d --build
docker-compose -f "docker-compose_update_quote_stream.yml" up -d --build