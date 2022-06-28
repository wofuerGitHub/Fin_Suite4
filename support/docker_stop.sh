#!/bin/bash
sudo docker ps -a
sudo docker stop update_fx_eur

sudo docker stop update_symbols_list
sudo docker stop update_cash_flow_statement

sudo docker stop update_company_key_stats
sudo docker stop update_balance_sheet_statement
sudo docker stop update_income_statement
sudo docker ps -a