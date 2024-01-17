-- solvesql 우리 플랫폼에 정착한 판매자1
-- https://solvesql.com/problems/settled-sellers-1/

SELECT seller_id, orders
FROM (
  SELECT seller_id, count(DISTINCT order_id) as orders
  FROM olist_order_items_dataset
  GROUP BY seller_id
)
WHERE orders >= 100

-- 한 주문(order_id) 안에 같은 판매자의 상품이 여러개 들어 있을 수 있음
-- 따라서 그냥 order_id 갯수가 아니라 DISTINCT order_id 갯수를 세어야 함