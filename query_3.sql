SELECT sg.name AS group_name, AVG(r.rate) AS average_rating
FROM students s
JOIN rating r ON s.id = r.students_id
JOIN students_groups sg ON s.students_groups = sg.id
WHERE r.subjects_id = ?
GROUP BY sg.id, sg.name
ORDER BY average_rating DESC;