-- Write query to get number of graded assignments for each student:
SELECT student_id, COUNT(*) as graded_count
FROM assignments
WHERE state = 'GRADED'
GROUP BY student_id
ORDER BY student_id;

-- Write query to get number of graded assignments for each student:
-- select student_id, count(id) as graded_assignments from assignments where state=='GRADED';