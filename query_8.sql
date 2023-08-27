SELECT t.name AS teacher_name, AVG(r.rate) AS average_rating
FROM teachers t
JOIN subjects sub ON t.id = sub.teachers_id
JOIN rating r ON sub.id = r.subjects_id
WHERE t.name = ?
GROUP BY t.name;