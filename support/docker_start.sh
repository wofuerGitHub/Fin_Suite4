#!/bin/bash
sudo docker ps -a

sudo docker start update_symbols_list
sudo docker start update_cash_flow_statement

sudo docker start update_company_key_stats
sudo docker start update_balance_sheet_statement
sudo docker start update_income_statement

sudo docker start update_fx_stream
sudo docker start update_quote_stream

sudo docker ps -a