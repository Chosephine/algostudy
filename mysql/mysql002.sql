-- programmers 경기도에 위치한 식품창고 목록 출력하기
CREATE TABLE FOOD_WAREHOUSE(
    WAREHOUSE_ID VARCHAR(10) NOT NULL AUTO_INCREMENT,
    WAREHOUSE_NAME VARCHAR(20) NOT NULL,
    ADDRESS VARCHAR(100) NULL,
    TLNO VARCHAR(20) NULL,
    FREEZER_YN VARCHAR(1) NULL,
);

SELECT
    WAREHOUSE_ID,
    WAREHOUSE_NAME,
    ADDRESS,
    IFNULL(FREEZER_YN, 'N') AS FREEZER_YN
FROM FOOD_WAREHOUSE
WHERE ADDRESS LIKE '경기도%'
ORDER BY
    WAREHOUSE_ID;

-- wildcard
-- % : 0개이상의 문자
-- _ : 임의의 단일 문자

