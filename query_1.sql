SELECT s.id, s.name, AVG(r.rate) AS average_rating 
FROM students s 
JOIN rating r ON s.id = r.students_id 
GROUP BY s.id, s.name 
ORDER BY average_rating 
DESC LIMIT 5;