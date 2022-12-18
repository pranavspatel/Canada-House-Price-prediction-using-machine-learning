-- Join house_price, immigrant and mortgage_rate table on date column
SELECT house_price."Date",house_price."Composite_HPI_SA",house_price."Composite_Benchmark_SA",
mortgage_rate."Rate"
INTO DB1
FROM house_price
RIGHT JOIN mortgage_rate 
	ON (house_price."Date"=mortgage_rate."Date")




