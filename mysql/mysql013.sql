-- programmers 133025 과일로 만든 아이스크림 고르기
SELECT FH.FLAVOR
FROM FIRST_HALF FH, ICECREAM_INFO II
WHERE FH.FLAVOR = II.FLAVOR AND 
    FH.TOTAL_ORDER >= 3000 AND II.INGREDIENT_TYPE = 'fruit_based'
ORDER BY FH.TOTAL_ORDER DESC;

-- join 쓰는 방법
SELECT FH.FLAVOR
FROM FIRST_HALF FH
    JOIN ICECREAM_INFO II ON FH.FLAVOR = II.FLAVOR
    -- mysql 은 join을 inner join으로 인식!
WHERE FH.TOTAL_ORDER >= 3000 AND II.INGREDIENT_TYPE = 'fruit_based'
ORDER BY FH.TOTAL_ORDER DESC;