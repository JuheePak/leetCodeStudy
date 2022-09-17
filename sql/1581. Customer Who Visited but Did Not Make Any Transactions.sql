-- Write your MySQL query statement below
-- LEFT OUTER JOIN
SELECT customer_id, COUNT(customer_id) AS count_no_trans
FROM Visits as v
LEFT OUTER JOIN Transactions as t
ON v.visit_id = t.visit_id
WHERE t.visit_id IS NULL
GROUP BY customer_id;
