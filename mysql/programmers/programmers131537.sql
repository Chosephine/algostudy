-- programmers 131537 오프라인/온라인 판매 데이터 통합하기
SELECT *
FROM (
    (SELECT 
        DATE_FORMAT(SALES_DATE, '%Y-%m-%d') AS SALES_DATE, 
        PRODUCT_ID, 
        USER_ID, 
        SALES_AMOUNT
    FROM ONLINE_SALE
    WHERE MONTH(SALES_DATE)=3)
    UNION ALL
    (SELECT 
        DATE_FORMAT(SALES_DATE, '%Y-%m-%d') AS SALES_DATE, 
        PRODUCT_ID, 
        NULL AS USER_ID, 
        SALES_AMOUNT
    FROM OFFLINE_SALE 
    WHERE MONTH(SALES_DATE)=3)
    ) A
ORDER BY A.SALES_DATE ASC, A.PRODUCT_ID ASC, A.USER_ID ASC;

-- MySQL Every derived table must have its own alias : 서브쿼리한테 이름 붙여줘야 함
-- 중복값을 나타내고 싶다면 UNION ALL, 아니면 UNION
-- UNION 사용 시 하나 의 ORDER BY만 사용 가능