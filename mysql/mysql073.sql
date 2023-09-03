-- 프로그래머스 157339 특정 기간동안 대여 가능한 자동차들의 대여비용 구하기

SELECT DISTINCT C.CAR_ID, C.CAR_TYPE, round((C.DAILY_FEE * 30) * (1-(TRIM(TRAILING '%' FROM D.DISCOUNT_RATE)/100)), -1) AS FEE
FROM CAR_RENTAL_COMPANY_CAR C
    LEFT JOIN (
        SELECT *
        FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
        WHERE START_DATE BETWEEN '2022-11-01' AND '2022-11-30'
            OR END_DATE BETWEEN '2022-11-01' AND '2022-11-30'
            OR (START_DATE <'2022-11-01' AND END_DATE > '2022-11-30')
    ) H ON C.CAR_ID=H.CAR_ID
    INNER JOIN (
        SELECT *
        FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN
        WHERE DURATION_TYPE LIKE '3%'
    ) D ON C.CAR_TYPE=D.CAR_TYPE
WHERE H.CAR_ID IS NULL
    AND C.CAR_TYPE IN ('세단', 'SUV')
    AND (C.DAILY_FEE * 30) * (1-(TRIM(TRAILING '%' FROM D.DISCOUNT_RATE)/100)) BETWEEN 500000 AND 2000000
ORDER BY FEE DESC, CAR_TYPE, CAR_ID DESC;

-- 이왜안요소1: H TABLE에서 세번째 WHERE 조건
-- 이왜안요소2: LEFT JOIN은 교집합도 포함임! (교집합을 빼려면 17 line이 필요하다)
-- 위와 관련하여 잘 정리해둔 링크: https://chlgpdus921.github.io/basecamp/MySQL-JOIN/
