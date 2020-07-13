-- script that displays the max temperature of each state 
SELECT state, max(VALUE) as max_temp FROM temperatures GROUP BY state ASC;