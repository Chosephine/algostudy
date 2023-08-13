-- 프로그래머스 164670 조건에 맞는 사용자 정보 조회하기
SELECT 
    A.USER_ID, 
    A.NICKNAME, 
    A.전체주소, 
    A.전화번호
FROM (
    SELECT 
        U.USER_ID, 
        U.NICKNAME, 
        CONCAT(U.CITY, ' ', U.STREET_ADDRESS1, ' ', U.STREET_ADDRESS2) AS 전체주소, 
        CONCAT(SUBSTR(U.TLNO, 1, 3), '-', SUBSTR(U.TLNO, 4, 4), '-', SUBSTR(U.TLNO, 8, 4)) AS 전화번호,
        COUNT(B.BOARD_ID) OVER (PARTITION BY U.USER_ID) AS CNT
    FROM USED_GOODS_BOARD B INNER JOIN USED_GOODS_USER U ON B.WRITER_ID=U.USER_ID
    ) A
WHERE CNT>=3
GROUP BY A.USER_ID
ORDER BY USER_ID DESC;

-- SUBSTR(str, position, len) 에서 position은 index를 뜻함.
--  position은 0부터 시작하고, 음수도 지원함.

-- CONCAT_WS 라는 function도 있음

-- GROUP BY에서 HAVING을 썼다면 이중쿼리를 안 써도 됨
