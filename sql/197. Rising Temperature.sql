-- Write your MySQL query statement below
SELECT t1.id
FROM (
SELECT id
       , temperature
       , recordDate
       , LAG(temperature, 1) OVER (ORDER BY recordDate) AS diff_temp
       , LAG(recordDate, 1) OVER (ORDER BY recordDate) AS diff_date
FROM Weather AS w) t1
WHERE temperature > t1.diff_temp
AND DATEDIFF(t1.diff_date, recordDate) = -1