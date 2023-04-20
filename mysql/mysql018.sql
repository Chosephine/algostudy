-- 프로그래머스 131536 재구매가 일어난 상품과 회원 리스트 구하기
SELECT USER_ID, PRODUCT_ID
FROM ONLINE_SALE
GROUP BY USER_ID, PRODUCT_ID
    HAVING COUNT(*) >= 2
ORDER BY USER_ID ASC, PRODUCT_ID DESC;

-- GROUP BY는 HAVING으로 조건 작성
-- GROUP BY는 SELECT문에 있는 칼럼이어야 함
-- 여러 기준으로 그룹핑하기 위해서는 여러 기준을 제시하면 됨