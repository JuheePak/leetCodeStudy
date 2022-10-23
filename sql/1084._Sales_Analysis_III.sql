-- Write your MySQL query statement below
SELECT P.product_id, P.product_name
FROM Product AS P
,(SELECT product_id, MAX(sale_date) AS max_sale_date, MIN(sale_date) AS min_sale_date
FROM Sales
GROUP BY product_id) AS S
WHERE P.product_id = S.product_id
    AND (S.max_sale_date BETWEEN '2019-01-01' AND '2019-03-31')
    AND (S.min_sale_date BETWEEN '2019-01-01' AND '2019-03-31');

