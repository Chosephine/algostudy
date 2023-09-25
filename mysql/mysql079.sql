-- leetcode 180. Consecutive Numbers(Medium)
-- https://leetcode.com/problems/consecutive-numbers/description/

/*
1) 3번 이상 연속으로 나타나는 숫자 나타내기
2) order 상관 없음
*/

WITH CTE AS (
  SELECT
    num, 
    LEAD(num) over () AS f, 
    LAG(num) over () AS b
  FROM Logs
)

SELECT DISTINCT num as ConsecutiveNums
FROM CTE
WHERE num=f AND num=b;

-- Lead() 는 현재 행 다음값, Lag() 는 현재 행 이전값을 가져 오는 함수
-- 그룹화, 정렬을 하고 싶지 않아도 MySQL8.0에서는 over () 을 반드시 붙여줘야 함!
-- 위 함수들은 "Window Function"임