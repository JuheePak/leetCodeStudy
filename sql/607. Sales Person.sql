-- Write your MySQL query statement below
SELECT SP.name
FROM SalesPerson AS SP
WHERE SP.sales_id NOT IN
(
SELECT O.sales_id
FROM Orders AS O
JOIN Company AS C ON O.com_id = C.com_id
WHERE C.name = 'RED');
