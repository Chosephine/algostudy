-- solvesql 멘토링 짝꿍 테스트
-- https://solvesql.com/problems/mentor-mentee-list/

-- 멘티 : 2021년 12월 31일을 기준으로 3개월 이내 입사
-- 멘토 : 2021년 12년 31일을 기준으로 재직한지 2년 이상
-- 서로 다른 부서에 속하는 직원끼리 멘토링 진행
-- 매칭 가능한 멘토가 없는 경우도 모두 포함
-- 멘티ID 기준 오름차순 정렬, 멘티1명에 배정 가능한 멘토가 여러 명인 경우 멘토ID로 오름차순 정렬

SELECT
  A.employee_id as mentee_id,
  A.name as mentee_name,
  B.employee_id as mentor_id,
  B.name as mentor_name
FROM
  employees A
  JOIN employees B
WHERE
  A.join_date >= '2021-09-31'
  AND B.join_date <= '2019-12-31'
  AND A.department != B.department
ORDER BY mentee_id ASC, mentor_id ASC;