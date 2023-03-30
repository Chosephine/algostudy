-- programmers 131535 조건에 맞는 회원수 구하기
SELECT count(*)
FROM USER_INFO 
WHERE YEAR(JOINED) = 2021 AND AGE >= 20 AND AGE <= 29;