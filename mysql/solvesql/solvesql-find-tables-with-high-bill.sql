-- solvesql 많이 주문한 테이블 찾기
-- https://solvesql.com/problems/find-tables-with-high-bill/

SELECT *
FROM tips
WHERE total_bill > (SELECT AVG(total_bill) FROM tips);