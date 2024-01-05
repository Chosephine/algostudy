-- 프로그래머스 151137 자동차 종류 별 특정 옵션이 포함된 자동차 수 구하기
SELECT CAR_TYPE, COUNT(*) AS CARS
FROM CAR_RENTAL_COMPANY_CAR
WHERE OPTIONS LIKE '%열선시트%' 
    OR OPTIONS LIKE '%통풍시트%' 
    OR OPTIONS LIKE '%가죽시트%'
GROUP BY CAR_TYPE
ORDER BY CAR_TYPE;
-- 1) OPTION에 시트 들어간건 다 포함이니까 LIKE '%시트%' 해도 됐을지도
-- 2) WHERE 문이 GROUP BY 뒤에 가면 에러가 난다. 
--    WHERE 문이 GROUP BY와 함께 쓰일 땐 위치가 중요함: WHERE이 우선이고, GROUP BY가 나중
--    WHERE로 먼저 데이터를 추출한 후에 GROUP BY로 집계해야 하기 때문
-- 3) REGEXP_LIKE(OPTIONS,'통풍시트|열선시트|가죽시트')