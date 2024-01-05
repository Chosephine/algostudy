-- 프로그래머스 131534 상품을 구매한 회원 비율 구하기

-- 2021년에 가입한 전체 회원들 중 
-- 상품을 구매한 회원수와 상품을 구매한 회원의 비율(=2021년에 가입한 회원 중 상품을 구매한 회원수 / 2021년에 가입한 전체 회원 수)을 년, 월 별로 출력
-- 상품을 구매한 회원의 비율은 소수점 두번째자리에서 반올림
-- 전체 결과는 년을 기준으로 오름차순 정렬해주시고 년이 같다면 월을 기준으로 오름차순 정렬

WITH CTE AS (
    SELECT U.USER_ID, S.ONLINE_SALE_ID, S.PRODUCT_ID, S.SALES_DATE
    FROM USER_INFO U INNER JOIN ONLINE_SALE S ON U.USER_ID=S.USER_ID
    WHERE YEAR(U.JOINED)=2021
)

SELECT 
    YEAR(CTE.sales_date) AS YEAR, 
    MONTH(CTE.sales_date) AS MONTH, 
    COUNT(DISTINCT CTE.USER_ID) AS PUCHASED_USERS, 
    ROUND(COUNT(DISTINCT CTE.USER_ID) / (SELECT COUNT(DISTINCT USER_ID) FROM USER_INFO WHERE YEAR(JOINED)=2021), 1) AS PUCHASED_RATIO
FROM CTE
GROUP BY YEAR, MONTH
ORDER BY YEAR, MONTH;

-- 사용자 정의 변수를 사용하면 PUCHASED_RATIO 에서 매번 쿼리를 날리지 않아도 된다..!
