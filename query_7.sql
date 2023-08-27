SELECT s.name AS student_name, r.rate
FROM students s
JOIN students_groups sg ON s.students_groups = sg.id
JOIN rating r ON s.id = r.students_id
JOIN subjects sub ON r.subjects_id = sub.id
WHERE sg.name = ?  
  AND sub.name = ?; 