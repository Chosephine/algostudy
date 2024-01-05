-- 프로그래머스 131116 식품분류별 가장 비싼 식품의 정보 조회하기
SELECT 
    A.*
FROM (
    SELECT 
        CATEGORY, 
        MAX(PRICE) OVER (PARTITION BY CATEGORY) AS MAX_PRICE, 
        CASE
            WHEN PRICE = MAX(PRICE) OVER (PARTITION BY CATEGORY)
            THEN PRODUCT_NAME
        END AS PRODUCT_NAME
    FROM FOOD_PRODUCT
    WHERE CATEGORY IN ('과자', '국', '김치', '식용유')
    ) A
WHERE A.PRODUCT_NAME IS NOT NULL
ORDER BY MAX_PRICE DESC;

-- A 테이블에서 GROUP BY CATEAGORY 절을 추가한 쿼리만 사용해서는 제대로 답이 안나온다 whyrano....?..

-- rank() 와 partition by 사용하는 방법도 있다!
-- ex. rank() over (partition by CATEGORY order by max(PRICE) desc) 
