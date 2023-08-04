-- 프로그래머스 59042 없어진 기록 찾기
SELECT O.ANIMAL_ID, O.NAME
FROM ANIMAL_INS I RIGHT OUTER JOIN ANIMAL_OUTS O ON I.ANIMAL_ID=O.ANIMAL_ID
WHERE I.ANIMAL_ID IS NULL
ORDER BY ANIMAL_ID;

-- 교집합 부분을 빼려면 WHERE ~ IS NULL 로 처리
-- 원래 MySQL은 INTERSECT나 EXCEPT와 같은 문법을 지원하지 않았으나 MySQL8.0 이상에서는 지원함
-- 보통 코테 MySQL서버는 5.7인 것으로 추정되므로 해당 기능을 사용할 수 없음!
