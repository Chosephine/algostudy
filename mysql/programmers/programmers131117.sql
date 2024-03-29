-- 프로그래머스 131117 5월 식품들의 총매출 조회하기
SELECT PR.PRODUCT_ID, PR.PRODUCT_NAME, SUM(PR.PRICE * O.AMOUNT) AS TOTAL_SALES
FROM FOOD_PRODUCT PR INNER JOIN FOOD_ORDER O ON PR.PRODUCT_ID=O.PRODUCT_ID
WHERE PRODUCE_DATE LIKE '2022-05%'
GROUP BY PRODUCT_ID
ORDER BY TOTAL_SALES DESC, PRODUCT_ID ASC;