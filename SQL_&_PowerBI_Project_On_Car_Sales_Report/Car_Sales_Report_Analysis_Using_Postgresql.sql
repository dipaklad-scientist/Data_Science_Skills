DROP TABLE IF EXISTS car_sales;
CREATE TABLE car_sales(
	car_id VARCHAR(20) PRIMARY KEY NOT NULL, 
	dates DATE, 
	customer_name CHAR(20),
	gender CHAR (10),
	annual_income INT,
	dealer_name VARCHAR(80),
	company VARCHAR(40),
	model VARCHAR(30),
	engine VARCHAR(60),
	transmission VARCHAR(30),
	color VARCHAR(10),
	price INT,
	dealer_no VARCHAR(12), 
	body_style VARCHAR(20),
	phone INT,
	dealer_region VARCHAR(30)
	);

SELECT DATE_TRUNC('month', dates)::DATE AS month,
	  COUNT(*) AS units_sold,SUM(price) AS revenue,
	  AVG(price) AS avg_selling_price FROM car_sales 
	  GROUP BY month ORDER BY month;


SELECT dealer_name,dealer_region,COUNT(*) AS units,
	  SUM(price) AS revenue,AVG(price) AS asp FROM car_sales
	  GROUP BY dealer_name, dealer_region ORDER BY revenue DESC, units DESC;


SELECT body_style,COUNT(*) AS units,AVG(price) AS avg_price,
  STDDEV_POP(price) AS price_stddev,MIN(price) AS min_price,
  MAX(price) AS max_price FROM car_sales GROUP BY body_style ORDER BY units DESC;


SELECT model,dealer_region,COUNT(*) AS units,
  SUM(price) AS revenue,AVG(price) AS asp FROM car_sales
  GROUP BY model, dealer_region ORDER BY units DESC, revenue DESC;


SELECT gender,dealer_region,
  SUM(CASE WHEN transmission = 'Auto' THEN 1 ELSE 0 END) AS automatic_units,
  SUM(CASE WHEN transmission = 'Manual' THEN 1 ELSE 0 END) AS manual_units,
  ROUND(100.0 * SUM(CASE WHEN transmission = 'Auto' THEN 1 ELSE 0 END) / COUNT(*), 1) AS automatic_share_pct
  FROM car_sales GROUP BY gender, dealer_region ORDER BY automatic_share_pct DESC;


SELECT company,engine,COUNT(*) AS units,
  AVG(price) AS avg_price FROM car_sales
  GROUP BY company, engine ORDER BY units DESC, avg_price DESC;




