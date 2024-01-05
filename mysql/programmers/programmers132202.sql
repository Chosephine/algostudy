-- 프로그래머스 132202 진료과별 총 예약 횟수 출력하기
SELECT MCDP_CD AS 진료과코드, COUNT(PT_NO) AS 5월예약건수
FROM APPOINTMENT 
WHERE APNT_YMD LIKE '2022-05%'
GROUP BY MCDP_CD
ORDER BY 5월예약건수 ASC, 진료과코드 ASC;

-- 1) COLUMN 명을 '진료과코드' '5월예약건수'로 지정했더니 ORDER BY가 먹히지 않는다
-- 2) COL 명을 '진료와코드', '5월예약건수'로 지정하고 ORDERY BY를 '~' 를 쓰면 정렬 안됨
--    근데 ORDER BY만 따옴표 떼면 됨
-- 3) MySQL would try to order your results by the string 'A', 
--    which isn't meaningful and won't give you the results you're expecting.
-- 4) 아무튼 MySQL은 바보야
