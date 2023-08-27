SELECT s.name AS student_name, AVG(r.rate) AS average_rating
FROM students s
JOIN rating r ON s.id = r.students_id
WHERE r.subjects_id = ?
GROUP BY s.id
ORDER BY average_rating DESC
LIMIT 1;