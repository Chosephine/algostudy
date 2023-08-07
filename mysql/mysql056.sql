-- 프로그래머스 151139 대여 횟수가 많은 자동차들의 월별 대여 횟수 구하기

--####### 이건 됨
SELECT A.MONTH, A.CAR_ID, COUNT(*) AS RECORDS
FROM (
    SELECT MONTH(START_DATE) AS MONTH, CAR_ID, COUNT(HISTORY_ID) OVER (PARTITION BY CAR_ID) AS CNT
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE 
        START_DATE LIKE '2022-08%' OR
        START_DATE LIKE '2022-09%' OR
        START_DATE LIKE '2022-10%' 
    ) A
WHERE CNT >= 5
GROUP BY MONTH, CAR_ID HAVING COUNT(*) > 0
ORDER BY MONTH ASC, CAR_ID DESC;

--####### 이건 안됨
SELECT A.MONTH, A.CAR_ID, COUNT(*) AS RECORDS
FROM (
    SELECT MONTH(START_DATE) AS MONTH, CAR_ID, COUNT(*) OVER (PARTITION BY CAR_ID) AS COUNT
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE 
        START_DATE LIKE '2022-08%' OR
        START_DATE LIKE '2022-09%' OR
        START_DATE LIKE '2022-10%' 
    GROUP BY CAR_ID HAVING COUNT >=5
    ) A
GROUP BY MONTH, CAR_ID HAVING COUNT(*) > 0
ORDER BY MONTH ASC, CAR_ID DESC;