-- leetcode 585. Investments in 2016
-- https://leetcode.com/problems/investments-in-2016/description/

/*
1) tiv_2016의 총합 계산, 소수점 2자리수까지
2) 근데 해당 주주의 tiv_2015가 다른 한 주주의 tiv_2015와 동일한
3) 근데 (lat, lon)이 unique한 
*/

-- C1: (lat, lon) 가 유일한 pid 를 찾기 위한 CTE
-- C2: 2015와 동일한 주주가 몇 명인지 체크하기 위한 CTE
WITH C1 AS (
    SELECT pid, lat, lon, count(*) as loc_cnt
    FROM Insurance
    GROUP BY lat, lon
), C2 AS (
    SELECT pid, tiv_2015, count(*) over (partition by tiv_2015) as 15_cnt
    FROM Insurance
)

SELECT ROUND(SUM(tiv_2016), 2) as tiv_2016
FROM Insurance
WHERE pid in (SELECT pid FROM C1 WHERE loc_cnt = 1) AND pid in (SELECT pid FROM C2 WHERE 15_cnt > 1)

-- round(col, decimal) 은 소수점 decimal 자리 수까지 반올림한다는 소리!