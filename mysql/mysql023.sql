-- 프로그래머스 59038 최솟값 구하기
SELECT MIN(DATETIME) AS '시간'
FROM ANIMAL_INS;

SELECT DATETIME AS '시간'
FROM ANIMAL_INS
ORDER BY DATETIME LIMIT 1;