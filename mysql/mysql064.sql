-- 프로그래머스 77487 헤비 유저가 소유한 장소
SELECT *
FROM PLACES
WHERE HOST_ID in (
    SELECT HOST_ID
    FROM PLACES
    GROUP BY HOST_ID HAVING COUNT(ID) > 1
    )
ORDER BY ID ASC;