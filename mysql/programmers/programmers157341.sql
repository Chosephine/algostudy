-- 프로그래머스 157341 대여 기록이 존재하는 자동차 리스트 구하기
SELECT DISTINCT H.CAR_ID
FROM CAR_RENTAL_COMPANY_CAR C INNER JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY H ON C.CAR_ID=H.CAR_ID
WHERE C.CAR_TYPE='세단' AND H.START_DATE LIKE '%-10-%'
ORDER BY CAR_ID DESC;