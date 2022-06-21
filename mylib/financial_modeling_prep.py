"""financial modeling prep module"""

#!/usr/bin/python3

from urllib.request import urlopen, HTTPError
import json
import certifi

def get_jsonparsed_data(url:str):
    """
    Receive the content of ``url``, parse it as JSON and return the object.

    Parameters
    ----------
    url : str

    Returns
    -------
    dict

    Tests
    -----
    


    """
    try:
        response = urlopen(url, cafile=certifi.where())
        data = response.read().decode("utf-8")
        return json.loads(data)
    except HTTPError as err:
        print(err.code)
        return {}

"""
tests:
- KSU^
"""
    


def get_financial_statement_list(api:str):
    """
    Receive the financial statement list.
    https://site.financialmodelingprep.com/developer/docs#Financial-Statements-List

    Parameters
    ----------
    api : str

    Returns
    -------
    list
    """
    url = "https://financialmodelingprep.com/api/v3/financial-statement-symbol-lists?apikey="+api
    return get_jsonparsed_data(url)

def get_symbols_list(api:str, **kwargs):
    """
    Receive the financial statement list.
    https://site.financialmodelingprep.com/developer/docs#Financial-Statements-List

    Parameters
    ----------
    api : str
    type : str

    Returns
    -------
    list
    """
    type = kwargs.get('type', 'stock')
    if type == 'etf':
        url = "https://financialmodelingprep.com/api/v3/etf/list?apikey="+api
    else:
        url = "https://financialmodelingprep.com/api/v3/stock/list?apikey="+api
    return get_jsonparsed_data(url)

def get_company_key_stats(company:str, api:str):
    """
    Receive the company key stats.
    https://site.financialmodelingprep.com/developer/docs/companies-key-stats-free-api#Python

    Parameters
    ----------
    api : str
    company : str

    Returns
    -------
    dict
    """
    url = "https://financialmodelingprep.com/api/v3/profile/"+company+"?apikey="+api
    return get_jsonparsed_data(url)

def get_income_statement(company:str, api:str):
    """
    Receive the company key stats.
    https://site.financialmodelingprep.com/developer/docs/companies-key-stats-free-api#Python

    Parameters
    ----------
    api : str
    company : str

    Returns
    -------
    dict
    """
    url = "https://financialmodelingprep.com/api/v3/income-statement/"+company+"?limit=10&apikey="+api
    return get_jsonparsed_data(url)

def get_balance_sheet_statement(company:str, api:str):
    """
    Receive the company key stats.
    https://site.financialmodelingprep.com/developer/docs/companies-key-stats-free-api#Python

    Parameters
    ----------
    api : str
    company : str

    Returns
    -------
    dict
    """
    url = "https://financialmodelingprep.com/api/v3/balance-sheet-statement/"+company+"?limit=10&apikey="+api
    return get_jsonparsed_data(url)

def get_cash_flow_statement(company:str, api:str):
    """
    Receive the company key stats.
    https://site.financialmodelingprep.com/developer/docs/companies-key-stats-free-api#Python

    Parameters
    ----------
    api : str
    company : str

    Returns
    -------
    dict
    """
    url = "https://financialmodelingprep.com/api/v3/cash-flow-statement/"+company+"?limit=10&apikey="+api
    return get_jsonparsed_data(url)
# print(get_company_key_stats('aapl', 'ab6801b4bddcf7ef835ca3850fd7333d'))
    