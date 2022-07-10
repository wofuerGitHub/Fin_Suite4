#!/bin/bash
docker ps -a

docker stop fmg_basic_symbolslist
docker stop fmg_basic_companykeystats

docker stop fmg_fun_income
docker stop fmg_fun_cashflow
docker stop fmg_fun_balancesheet

docker stop fmg_load_quote
docker stop fmg_load_fx

docker stop fmg_stream_quote
docker stop fmg_stream_fx

docker ps -a