# Write your MySQL query statement below

SELECT U.user_id AS buyer_id
    , U.join_date
    , sum(case when O.order_date like '2019%' then 1 else 0 end) as orders_in_2019
FROM Users AS U
LEFT JOIN Orders AS O On U.user_id = O.buyer_id
GROUP BY U.user_id