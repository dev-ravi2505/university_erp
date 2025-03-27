from odoo import fields, models


class SemesterInfo(models.Model):
    _name = "semester.info"
    _description = "Semester Information"
    _rec_name = "name"

    name = fields.Char(string='Name')
    department_info_id = fields.Many2one('department.info',string='Department', required=True)
    semester_number = fields.Integer(string='Semester', required=True)