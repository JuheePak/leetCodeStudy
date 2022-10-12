# Write your MySQL query statement below
SELECT U.name, IFNULL(D.distance, 0) AS travelled_distance
FROM Users AS U
LEFT JOIN
(SELECT user_id, sum(distance) AS distance
FROM Rides
GROUP BY user_id) AS D ON U.id = D.user_id
ORDER BY travelled_distance DESC, name ASC;