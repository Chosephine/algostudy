-- leetcode 175. Combine Two Tables (Easy)
-- https://leetcode.com/problems/combine-two-tables/description/

/*
1) Person table 에 있는 값이 Address table 에 없으면 null
2) order 상관 없음
*/

SELECT P.firstName, P.lastName, A.city, A.state
FROM Person P LEFT JOIN Address A ON P.personId = A.personId