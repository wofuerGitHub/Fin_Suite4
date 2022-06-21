SELECT ins.date, ins.symbol, ins.reportedCurrency, ins.calendarYear, ins.period,
	ins.netIncome/ins.weightedAverageShsOut as 'eps', 
	-cfs.dividendsPaid/ins.weightedAverageShsOut as 'dps', # https://corporatefinanceinstitute.com/resources/knowledge/finance/dividend-per-share/
	cfs.operatingCashFlow/ins.weightedAverageShsOut as 'cps',
    (bss.totalStockholdersEquity-bss.preferredStock)/ins.weightedAverageShsOut as 'bps' # https://corporatefinanceinstitute.com/resources/knowledge/valuation/book-value-per-share-bvps/
    FROM fmg.incomestatement ins
LEFT JOIN fmg.cashflowstatement cfs
ON ins.symbol = cfs.symbol AND ins.date = cfs.date AND ins.reportedCurrency = cfs.reportedCurrency
LEFT JOIN fmg.balancesheetstatement bss
ON ins.symbol = bss.symbol AND ins.date = bss.date AND ins.reportedCurrency = bss.reportedCurrency;