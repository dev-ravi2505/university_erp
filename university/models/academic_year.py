from odoo import fields, models
from datetime import date


class AcademicYearInfo(models.Model):
    _name = "academic.year.info"
    _description = "Academic Year Information"
    _rec_name = "name"

    name = fields.Char(string='Name')
    start_date = fields.Date(string='Start Date', required=True)
    end_date = fields.Date(string='End Date', required=True)
    active_button = fields.Boolean(string='Active')