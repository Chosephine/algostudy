-- 프로그래머스 151141 자동차 대여 기록 별 대여 금액 구하기

WITH CAR_AND_HISTORY AS (
    SELECT H.HISTORY_ID, C.CAR_TYPE, C.DAILY_FEE, H.START_DATE, H.END_DATE, DATEDIFF(H.END_DATE, H.START_DATE) + 1 AS DAYS
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY H
        INNER JOIN CAR_RENTAL_COMPANY_CAR C ON C.CAR_ID=H.CAR_ID
    WHERE CAR_TYPE='트럭'
), PLAN AS (
    SELECT PLAN_ID, CAR_TYPE, DISCOUNT_RATE,
        TRIM(TRAILING '일 이상' FROM DURATION_TYPE) AS DT, 
        (100 - TRIM(TRAILING '%' FROM DISCOUNT_RATE))/100 AS DR
    FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN
    WHERE CAR_TYPE='트럭'
)

SELECT DISTINCT CH.HISTORY_ID,
    CASE 
        WHEN DAYS < 7 THEN ROUND(CH.DAILY_FEE * DAYS)
        WHEN DAYS < 30 THEN ROUND(CH.DAILY_FEE * DAYS * (SELECT DR FROM PLAN WHERE DT=7))
        WHEN DAYS < 90 THEN ROUND(CH.DAILY_FEE * DAYS * (SELECT DR FROM PLAN WHERE DT=30))
        ELSE ROUND(CH.DAILY_FEE * DAYS * (SELECT DR FROM PLAN WHERE DT=90))
        END AS FEE
FROM CAR_AND_HISTORY CH
    INNER JOIN PLAN P ON CH.CAR_TYPE=P.CAR_TYPE
ORDER BY FEE DESC, HISTORY_ID DESC;

-- CTE 정의할 때 WITH는 한 번만 써야함!
-- TRIM 문법 잊지 말기
