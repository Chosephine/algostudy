-- 프로그래머스 144855 카테고리 별 도서 판매량 집계하기

SELECT B.CATEGORY, SUM(BS.SALES) AS TOTAL_SALES
FROM BOOK B INNER JOIN BOOK_SALES BS ON B.BOOK_ID=BS.BOOK_ID
WHERE SALES_DATE LIKE '2022-01-%'
GROUP BY CATEGORY
ORDER BY CATEGORY ASC;

-- GROUP BY 절은 WHERE 절 뒤에 있어야 오류가 나지 않음..! (저번에 공부했으면서ㅠ)
-- <sequence of operations in SQL> 
-- -- FROM clause (including JOINs)
-- -- WHERE clause
-- -- GROUP BY clause
-- -- HAVING clause
-- -- SELECT clause
-- -- ORDER BY clause