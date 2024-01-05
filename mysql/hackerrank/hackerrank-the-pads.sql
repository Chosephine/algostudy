-- 해커랭크 The PADS (Intermediate)
-- https://www.hackerrank.com/challenges/the-pads/problem?isFullScreen=true

/*
1) 알파벳 순으로 정렬, occupations에 있는 이름, 
    ASingerName(S)의 형태
2) occupation 갯수, 오름차순으로 정렬, 두번째 정렬조건은 occupation 알파벳순,
    "There are a total of [occupation_count] [occupation]s."의 형태
*/

SELECT CONCAT(Name, '(', LEFT(Occupation, 1) ,')')
FROM OCCUPATIONS
ORDER BY Name;

SELECT CONCAT('There are a total of ', A.CNT, ' ' , lower(A.Occupation), 's.')
FROM (
    SELECT Occupation, Count(*) as CNT
    FROM OCCUPATIONS
    GROUP BY Occupation
    ORDER BY CNT ASC, Occupation ASC
) A;

-- 출력 예시 잘 보기..!
---- 테이블엔 Doctor 이지만 출력은 doctor 이었다!