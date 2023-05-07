-- 프로그래머스 157343 특정 옵션이 포함된 자동차 리스트 구하기
SELECT *
FROM CAR_RENTAL_COMPANY_CAR
WHERE OPTIONS LIKE '%네비게이션%'
ORDER BY CAR_ID DESC;

-- REGEX
-- % : matches any number of characters, even zero characters.
-- _ : matches exactly one character.

-- SELECT 문에서 LIKE 사용 시 boolean값으로 나옴
SELECT CAR_ID, CAR_TYPE, DAILY_FEE, OPTIONS LIKE '%네비게이션%'
FROM CAR_RENTAL_COMPANY_CAR
ORDER BY CAR_ID DESC;

-- WHERE문에서 locate('네비게이션', options) 도 사용 가능
-- MySQL에서 0은 false, 0 이외에는 true로 인식