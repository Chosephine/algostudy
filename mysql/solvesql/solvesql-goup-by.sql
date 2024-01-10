-- solvesql 데이터 그룹으로 묶기
-- https://solvesql.com/problems/group-by/

-- 분류는 group by지만 subquery로 풀었음
-- sqllite에는 표준편차 관련 함수가 없어서 아주 골머리였다^_^
SELECT
  distinct quartet,
  round(x_mean, 2) as x_mean,
  round(
    (SUM(x_deviation * x_deviation) over (PARTITION BY quartet)/(cnt - 1)), 2) as x_var,
  round(y_mean, 2) as y_mean,
  round(
    (SUM(y_deviation * y_deviation) over (PARTITION BY quartet)) / (cnt - 1),2) as y_var
FROM
  (
    SELECT
      quartet,
      avg(x) over (PARTITION by quartet) as x_mean,
      avg(y) over (PARTITION by quartet) as y_mean,
      x - avg(x) over (PARTITION by quartet) as x_deviation,
      y - avg(y) over (PARTITION by quartet) as y_deviation,
      count(*) over (PARTITION BY quartet) as cnt
    FROM
      points
  )

-- 문제에 맞게 GROUP BY 사용하여 리팩토링
-- WINDOWN 함수를 빼고 GROUP BY + 집계함수를 사용하면 동일한 결과를 얻을 수 있다.

SELECT
  quartet,
  round(x_mean, 2) as x_mean,
  round((SUM(x_deviation * x_deviation)/(cnt - 1)), 2) as x_var,
  round(y_mean, 2) as y_mean,
  round((SUM(y_deviation * y_deviation)/(cnt - 1)), 2) as y_var
FROM
  (
    SELECT
      quartet,
      avg(x) over (PARTITION by quartet) as x_mean,
      avg(y) over (PARTITION byquartet) as y_mean,
      x - avg(x) over (PARTITION by quartet) as x_deviation,
      y - avg(y) over (PARTITION by quartet) as y_deviation,
      count(*) over (PARTITION BY quartet) as cnt
    FROM
      points
  )
  GROUP BY
    quartet