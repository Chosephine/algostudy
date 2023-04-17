-- programmers 131120 3월에 태어난 여성 회원 목록 출력하기
SELECT MEMBER_ID, MEMBER_NAME, GENDER, DATE_FORMAT(DATE_OF_BIRTH, '%Y-%m-%d') as DATE_OF_BIRTH
FROM MEMBER_PROFILE
WHERE MONTH(DATE_OF_BIRTH)=03 AND GENDER='W' AND TLNO IS NOT NULL
ORDER BY MEMBER_ID ASC;

-- docs 상에서는 date() 함수를 활용할 수 있을 것 같은데 프로그래머스에서는 먹히지 않음
-- 해당 함수는 MySQL 4.1.1 버전부터 사용가능하다는 것으로 보아 프로그래머스 mysql은 4.1.1 버전보다 낮은 게 아닐까 추정!