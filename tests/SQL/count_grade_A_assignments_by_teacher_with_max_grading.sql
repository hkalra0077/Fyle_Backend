-- Write query to find the number of grade A's given by the teacher who has graded the most assignments
-- /home/abhigawande/Desktop/fyleproject/fyle-interview-intern-backend/tests/SQL/count_grade_A_assignments_by_teacher_with_max_grading.sql
-- WITH teacher_grading_counts AS (
--     SELECT teacher_id, COUNT(*) as graded_count
--     FROM assignments
--     WHERE state = 'GRADED'
--     GROUP BY teacher_id
-- ),
-- max_grading_teacher AS (
--     SELECT teacher_id
--     FROM teacher_grading_counts
--     WHERE graded_count = (SELECT MAX(graded_count) FROM teacher_grading_counts)
--     LIMIT 1
-- )
-- SELECT COUNT(*) as grade_a_count
-- FROM assignments
-- WHERE teacher_id = (SELECT teacher_id FROM max_grading_teacher)
--   AND grade = 'A'
--   AND state = 'GRADED';



SELECT
    COUNT(*) AS no_of_As
FROM
    assignments
WHERE
    grade == 'A'
GROUP BY
    teacher_id
ORDER BY
    no_of_As DESC;