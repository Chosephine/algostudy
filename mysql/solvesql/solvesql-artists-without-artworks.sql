-- solvesql 작품이 없는 작가 찾기
-- https://solvesql.com/problems/artists-without-artworks/

-- table: artists, artworks, 
-- MoMA에 등록된 작가, 현재 살아 있지 않은 작가 중 MoMA에 등록된 작품이 없는 작가
-- 작가의 ID와 이름

-- artists 테이블은 MoMA에 등록된 작가의 정보
-- artworks_artists 테이블은 작품에 참여한 작가들의 정보가 담긴 N:M 연관 테이블
-- point: artworks_artists 테이블에 등록된 작품들은 전시된 작품 => left join을 쓰면 된다!
-- LEFT OUTER JOIN은 A - B가 아니라 A라는 점..!

SELECT a.artist_id, a.name
FROM artists a LEFT OUTER JOIN artworks_artists b ON a.artist_id=b.artist_id
WHERE a.death_year IS NOT NULL AND b.artist_id IS NULL;




-- 아래쪽은 너무 어렵게 생각한 흔적..^^
-- duration과 전시 여부는 아무 상관이 없어ㄸr..ㅎㅎ

WITH artists_duration AS (
  SELECT distinct c.artist_id, SUM(b.duration) as sum_of_duration
  FROM artworks b, artworks_artists c
  WHERE b.artwork_id = c.artwork_id
  GROUP BY c.artist_id
)

SELECT a.artist_id, a.name, d.sum_of_duration
FROM artists a, artists_duration d
WHERE d.sum_of_duration IS NULL AND a.death_year IS NOT NULL;

-- 아래는 몬가 확인한 흔적

SELECT
  a.artist_id,
  SUM(b.duration) AS duration
FROM
  artists a,
  artworks_artists c, 
WHERE
  a.artist_id = c.artist_id
  AND a.death_year IS NOT NULL
GROUP BY
  a.artist_id
-- ORDER BY duration DESC
LIMIT 50


SELECT *
FROM artworks
ORDER BY duration asc
LIMIT 300

SELECT distinct c.artist_id, SUM(b.duration)
FROM artworks b, artworks_artists c
WHERE b.artwork_id = c.artwork_id
GROUP BY c.artist_id
ORDER BY b.duration desc