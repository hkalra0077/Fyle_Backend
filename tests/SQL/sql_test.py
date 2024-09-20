import random
from sqlalchemy import text

from core import db
from core.models.assignments import Assignment, AssignmentStateEnum, GradeEnum


def create_n_graded_assignments_for_teacher(number: int = 0, teacher_id: int = 1, a_grades: int = 0) -> int:
    grade_a_counter = Assignment.filter(
        Assignment.teacher_id == teacher_id,
        Assignment.grade == GradeEnum.A
    ).count()

    # Create assignments with exact 'A' grades as specified
    for _ in range(a_grades):
        assignment = Assignment(
            teacher_id=teacher_id,
            student_id=1,
            grade=GradeEnum.A,  # Force 'A' grade
            content='test content',
            state=AssignmentStateEnum.GRADED
        )
        db.session.add(assignment)
        grade_a_counter += 1

    # Create the remaining assignments with random grades
    for _ in range(number - a_grades):
        grade = random.choice(list(GradeEnum))
        assignment = Assignment(
            teacher_id=teacher_id,
            student_id=1,
            grade=grade,
            content='test content',
            state=AssignmentStateEnum.GRADED
        )
        db.session.add(assignment)
        if grade == GradeEnum.A:
            grade_a_counter += 1

    db.session.commit()
    return grade_a_counter


def test_get_grade_A_assignments_for_teacher_with_max_grading():
    """Test to get count of grade A assignments for teacher who has graded the most assignments"""

    # Read the SQL query from a file
    with open('tests/SQL/count_grade_A_assignments_by_teacher_with_max_grading.sql', encoding='utf8') as fo:
        sql = fo.read()

    # Create and grade 5 assignments for the default teacher (teacher_id=1), ensuring 4 'A' grades
    grade_a_count_1 = create_n_graded_assignments_for_teacher(5, a_grades=4)

    # Execute the SQL query and check if the count matches the created assignments
    sql_result = db.session.execute(text(sql)).fetchall()
    assert grade_a_count_1 == sql_result[0][0]

    # Create and grade 10 assignments for a different teacher (teacher_id=2), ensuring 10 'A' grades
    grade_a_count_2 = create_n_graded_assignments_for_teacher(10, 2, a_grades=10)

    # Execute the SQL query again and check if the count matches the newly created assignments
    sql_result = db.session.execute(text(sql)).fetchall()
    assert grade_a_count_2 == sql_result[0][0]

