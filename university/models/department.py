from odoo import fields, models


class DepartmentInfo(models.Model):
    _name = "department.info"
    _description = "Department Information"
    _rec_name = "name"

    name = fields.Char(string='Name')
    course_info_id = fields.Many2one('course.info', string='Course', required=True)
    course_code = fields.Char(string='Code', required=True)
    semester_info_ids = fields.One2many('semester.info', 'department_info_id', string='Semester')
