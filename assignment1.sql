SELECT
    toStartOfMonth(pickup_datetime) AS month,

    SUM(CASE WHEN dayOfWeek(pickup_datetime) = 6 THEN 1 ELSE 0 END) / COUNT(DISTINCT CASE WHEN dayOfWeek(pickup_datetime) = 6 THEN toStartOfWeek(pickup_datetime) ELSE NULL END) AS avg_saturday_trip_count,
    AVG(CASE WHEN dayOfWeek(pickup_datetime) = 6 THEN fare_amount ELSE NULL END) AS avg_saturday_fare,
    AVG(CASE WHEN dayOfWeek(pickup_datetime) = 6 THEN dateDiff('minute', pickup_datetime, dropoff_datetime) ELSE NULL END) AS avg_saturday_duration,

    SUM(CASE WHEN dayOfWeek(pickup_datetime) = 7 THEN 1 ELSE 0 END) / COUNT(DISTINCT CASE WHEN dayOfWeek(pickup_datetime) = 7 THEN toStartOfWeek(pickup_datetime) ELSE NULL END) AS avg_sunday_trip_count,
    AVG(CASE WHEN dayOfWeek(pickup_datetime) = 7 THEN fare_amount ELSE NULL END) AS avg_sunday_fare,
    AVG(CASE WHEN dayOfWeek(pickup_datetime) = 7 THEN dateDiff('minute', pickup_datetime, dropoff_datetime) ELSE NULL END) AS avg_sunday_duration
FROM tripdata
WHERE
    pickup_datetime BETWEEN '2014-01-01 00:00:00' AND '2016-12-31 23:59:59'
GROUP BY
    month
ORDER BY
    month;
