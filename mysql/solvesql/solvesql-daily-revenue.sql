-- solvesql 레스토랑의 일일 매출
-- https://solvesql.com/problems/daily-revenue/

SELECT day, revenue_daily
FROM
  (
    SELECT day, SUM(total_bill) as revenue_daily
    FROM tips
    GROUP BY day
  )
WHERE revenue_daily >= 1000
ORDER BY revenue_daily DESC;