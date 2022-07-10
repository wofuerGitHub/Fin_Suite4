#!/bin/bash
docker ps -a

docker start fmg_basic_symbolslist
docker start fmg_basic_companykeystats

docker start fmg_fun_income
docker start fmg_fun_cashflow
docker start fmg_fun_balancesheet

docker start fmg_load_quote
docker start fmg_load_fx

docker start fmg_stream_quote
docker start fmg_stream_fx

docker ps -a