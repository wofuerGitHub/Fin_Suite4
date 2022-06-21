/* finds all symbols in symbolslist that are not in companykeystats and adds theme there */

INSERT INTO fmg.companykeystats (symbol) SELECT a.symbol FROM fmg.symbolslist a
LEFT JOIN fmg.companykeystats b
ON a.symbol = b.symbol
WHERE b.symbol IS NULL;