from flask import Blueprint
from core import db
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.assignments import Assignment,Teacher
from .schema import AssignmentSchema, AssignmentGradeSchema,TeacherSchema
from core import db

principal_resources = Blueprint('principal_resources', __name__)

@principal_resources.route('/assignments', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_assignments(p):
    """Returns list of all submitted and graded assignments"""
    assignments = Assignment.get_all_submitted_and_graded()
    assignments_dump = AssignmentSchema().dump(assignments, many=True)
    return APIResponse.respond(data=assignments_dump)


@principal_resources.route("/teachers", methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_teachers(p):
    """ Returns a list of  the Teachers. """
    teachers = Teacher.list_teachers()
    teachers_dump = TeacherSchema().dump(teachers, many=True)
    return APIResponse.respond(data=teachers_dump)


# POST /principal/assignments/grade
@principal_resources.route("/assignments/grade", methods=['POST'] , strict_slashes=False)
@decorators.accept_payload
@decorators.authenticate_principal
def grade_assignments(p, incoming_payload):
    assignment_to_grade_payload = AssignmentGradeSchema().load(incoming_payload)

    graded_assignment = Assignment.regrade(
        _id=assignment_to_grade_payload.id,
        grade=assignment_to_grade_payload.grade
        )
    
    db.session.commit()

    graded_assignment_dump = AssignmentSchema().dump(graded_assignment)
    return APIResponse.respond(data=graded_assignment_dump)

