-- solvesql 배송 예정일 예측 성공과 실패
-- https://solvesql.com/problems/estimated-delivery-date/

-- olist_orders_dataset
-- process: 고객구매 - 주문승인 - 배송 시작 - 배송완료

-- 주문 배송 예측이 정확했는지 분석
-- 고객 구매 일자별 / 배송예정시각 within or not / 배송 완료 또는 배송 시작 데이터가 없는 경우는 계산에서 제외
-- purchase_date, success, fail 


WITH middle AS (
  SELECT
  DATE(order_purchase_timestamp) AS purchase_date,
  order_delivered_customer_date,
  order_estimated_delivery_date,
  STRFTIME('%s', order_delivered_customer_date) - STRFTIME('%s', order_estimated_delivery_date) AS diff
FROM
  olist_orders_dataset
WHERE
  order_purchase_timestamp LIKE '2017-01-%'
  AND order_delivered_customer_date IS NOT NULL
  AND order_estimated_delivery_date IS NOT NULL
)

SELECT
  distinct purchase_date,
  COUNT(CASE WHEN diff <= 0 THEN 1 END) OVER (PARTITION BY purchase_date) as success,
  COUNT(CASE WHEN diff > 0 THEN 1 END) OVER (PARTITION BY purchase_date) as fail
FROM middle
ORDER BY purchase_Date ASC;

-- SQL에서 조건에 따른 count는 COUNT와 CASE를 조합해서 사용
-- MySQL에서는 DATEDIFF 함수를 사용할 수 있다
-- SQLite docs에 TIMEDIFF라는 함수가 있지만 solvesql에선 먹히지 않음..!
---- strftime() 이라는 함수를 통해 직접 게산할 수 있다