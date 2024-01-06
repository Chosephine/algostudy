-- 프로그래머스 131124 그룹별 조건에 맞는 식당 목록 출력하기
SELECT M.MEMBER_NAME, R.REVIEW_TEXT, DATE_FORMAT(R.REVIEW_DATE, '%Y-%m-%d') AS REVIEW_DATE
FROM MEMBER_PROFILE M INNER JOIN REST_REVIEW R ON M.MEMBER_ID=R.MEMBER_ID
WHERE M.MEMBER_ID=(
    SELECT M.MEMBER_ID
    FROM MEMBER_PROFILE M INNER JOIN REST_REVIEW R ON M.MEMBER_ID=R.MEMBER_ID
    ORDER BY COUNT(R.REVIEW_ID) OVER (PARTITION BY R.MEMBER_ID) DESC LIMIT 1
)
ORDER BY REVIEW_DATE ASC, REVIEW_TEXT ASC;