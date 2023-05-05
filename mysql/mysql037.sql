-- 프로그래머스 151138 자동차 대여 기록에서 장기/단기 대여 구분하기
SELECT
    HISTORY_ID,
    CAR_ID,
    DATE_FORMAT(START_DATE, '%Y-%m-%d') AS START_DATE,
    DATE_FORMAT(END_DATE, '%Y-%m-%d') AS END_DATE,
    IF (DATEDIFF(END_DATE, START_DATE)>=29, '장기대여', '단기대여') AS RENT_TYPE
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE START_DATE LIKE '2022-09-%'
ORDER BY HISTORY_ID DESC;

-- 띄어쓰기 때문에 맞왜틀 20분...
-- LEFT(START_DATE, 10) 하면 yyyy-mm-dd 만 나옴!! 
-- IF 대신 'CASE WHEN 조건 THEN 결과 ELSE 다른결과' 문도 가능!