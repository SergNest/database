SELECT s.name AS subject_name
FROM subjects s
JOIN teachers t ON s.teachers_id = t.id
WHERE t.name = ?;