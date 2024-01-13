-- solvesql 많이 주문한 테이블 찾기
-- https://solvesql.com/problems/find-tables-with-high-bill/

-- ver.sqlite
SELECT *
FROM tips
WHERE total_bill > (SELECT AVG(total_bill) FROM tips);

-- ver.mysql : 변수선언 활용
-- 이게 문제 풀때도 적용되는지는 확인이 필요한 것 같다. 다음에 mysql 쿼리 문제 풀 대 한 번 해보기!

-- 변수 선언
SET @avg_total_bill = (SELECT AVG(total_bill) FROM tips);

-- 본쿼리
SELECT *
FROM tips
WHERE total_bill > @avg_total_bill;