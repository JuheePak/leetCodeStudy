-- Write your MySQL query statement below
SELECT U.name, SUM(T.amount) AS balance
FROM Users AS U, Transactions AS T
WHERE U.account = T.account
GROUP BY T.account
HAVING SUM(T.amount) > 10000