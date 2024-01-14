-- solvesql 첫 주문과 마지막 주문
-- https://solvesql.com/problems/first-and-last-orders/

SELECT
  SUBSTR(MIN(order_purchase_timestamp), 0, 11) as first_order_date,
  SUBSTR(MAX(order_purchase_timestamp), 0, 11) as last_order_date
FROM
  olist_orders_dataset