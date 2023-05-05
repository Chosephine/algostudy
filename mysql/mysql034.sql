-- programmers 133026 성분으로 구분한 아이스크림 총 주문량
SELECT I.INGREDIENT_TYPE, SUM(TOTAL_ORDER) AS TOTAL_ORDER
FROM FIRST_HALF F INNER JOIN ICECREAM_INFO I ON F.FLAVOR=I.FLAVOR
GROUP BY I.INGREDIENT_TYPE
ORDER BY TOTAL_ORDER ASC;