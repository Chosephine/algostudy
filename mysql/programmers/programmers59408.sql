-- 프로그래머스 59408 중복 제거하기
SELECT COUNT(DISTINCT NAME)
FROM ANIMAL_INS
WHERE NAME is not null;

-- 중복값 제거는 DISTNCT로
-- null이 아닌 값은 is not null 붙여서
