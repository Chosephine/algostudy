-- solvesql 최근 올림픽이 개최된 도시
-- https://solvesql.com/problems/olympic-cities/

SELECT year, upper(substr(city, 0, 4)) as city
FROM games
WHERE year >= 2000
ORDER BY year DESC;