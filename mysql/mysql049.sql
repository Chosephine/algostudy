 -- 프로그래머스 131113 조건별로 분류하여 주문상태 출력하기

SELECT ORDER_ID, 
        PRODUCT_ID, 
        DATE_FORMAT(OUT_DATE, '%Y-%m-%d') AS OUT_DATE,
        CASE
            WHEN OUT_DATE IS NULL THEN '출고미정'
            WHEN DATEDIFF(OUT_DATE, '2022-05-01') > 0 THEN '출고대기'
            ELSE '출고완료' END AS 출고여부
FROM FOOD_ORDER
ORDER BY ORDER_ID ASC;

-- CASE문은 두 방법으로 사용가능
-- 1) CASE [value] WHEN [compare_value1] THEN [result1] ... ELSE [result] END
-- 2) CASE WHEN [condition1] THEN [result1] ... ELSE [result] END