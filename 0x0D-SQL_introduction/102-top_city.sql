-- script that displays the top 3 of cities temperature
SELECT city, AVG(VALUE) as avg_temp FROM temperatures WHERE month = 7 or month = 8 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;