-- 프로그래머스 131529 카테고리 별 상품 개수 구하기

SELECT LEFT(PRODUCT_CODE, 2) AS CATEGORY, COUNT(*)
FROM PRODUCT
GROUP BY CATEGORY
ORDER BY CATEGORY ASC;