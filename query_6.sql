SELECT s.name
FROM students s
JOIN students_groups sg ON s.students_groups = sg.id
WHERE sg.name = ?;