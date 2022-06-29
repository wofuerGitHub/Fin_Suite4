SELECT a.*, b.`close` as `close`, a.`eps`/b.`close` as `eps_eur`, a.`dps`/b.`close` as `dps_eur`, a.`cps`/b.`close` as `cps_eur`, a.`bps`/b.`close` as `bps_eur` 
FROM fmg.edcbps a
LEFT JOIN fmg.fx_eur b
ON a.`date` = b.`date` AND a.`reportedCurrency` = b.`symbol`
WHERE a.`reportedCurrency` <> 'EUR'
UNION
SELECT c.*, 1 as `close`, c.eps as `eps_eur`, c.dps as `dps_eur`, c.cps as `cps_eur`, c.bps as `bps_eur`
FROM fmg.edcbps c
WHERE c.`reportedCurrency` = 'EUR';