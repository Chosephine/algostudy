-- solvesql 가구 판매의 비중이 높았던 날 찾기
-- https://solvesql.com/problems/day-of-furniture/


-- ver.1 결과 case가 7개라서 실패
SELECT order_date, furniture, round(((furniture+0.00)/ (all_count+0.00)) * 100, 3) as furniture_pct
FROM (
  SELECT order_date, count(order_id) as all_count, count(case when category='Furniture' then 1 end) as furniture
  FROM records
  GROUP BY order_date
)
WHERE all_count >= 10 and furniture_pct >= 40
ORDER BY furniture_pct DESC, order_date ASC

-- ver.2 구글링의 도움으로 자료 갯수는 맞췄는데..? 데이터가 틀린게 있다..?
SELECT
  order_date,
  furniture,
  round(
    ((furniture + 0.00) / (all_count + 0.00)) * 100, 2
  ) as furniture_pct
FROM
  (
    SELECT
      order_date,
      count(distinct order_id) as all_count,
      count( 
        distinct(case
          when category = 'Furniture' then order_id
        end)
      ) as furniture
    FROM
      records
    GROUP BY
      order_date
  )
WHERE all_count >= 10 and furniture_pct >= 40
ORDER BY
  furniture_pct DESC,
  order_date ASC

-- 참고 : https://milkyspace.tistory.com/90