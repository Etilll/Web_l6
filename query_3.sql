SELECT group_id, averages FROM (SELECT *, avg(value) as averages FROM marks m LEFT JOIN students s ON m.student_id = s.id WHERE subject_id = 4 GROUP BY group_id ORDER BY avg(value) DESC) LIMIT 1