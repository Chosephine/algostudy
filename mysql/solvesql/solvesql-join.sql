-- solvesql 두 테이블 결합하기
-- https://solvesql.com/problems/join/

SELECT
  distinct r.athlete_id
FROM
  events e
  JOIN records r ON e.id = r.event_id
WHERE
  e.sport = 'Golf';

-- 중복 제거를 위해 GROUP BY를 사용하는 경우가 많다.
-- 하지만 단순히 중복제거를 위해서라면 GROUP BY 보다는 DISTINCT가 가독성이 더 좋은 듯! 
-- 참고: https://kghworks.tistory.com/97