SELECT name, value, group_id FROM (SELECT * FROM marks m LEFT JOIN students s ON m.student_id = s.id WHERE subject_id = 4 AND group_id = 2)