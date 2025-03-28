from email.policy import default

from odoo import fields, models, api


class AttendanceInfo(models.Model):
    _name = "attendance.info"
    _description = "Attendance"

    student_info_id = fields.Many2one('student.info',string='Name', required=True)
    batch_info_id = fields.Many2one('batch.info', string='Batch', required=True, related='student_info_id.batch_info_id')
    date = fields.Date(string='Date', default=lambda self: fields.Date.context_today(self))
    is_present = fields.Boolean(string='Is Present', readonly=True)
    time = fields.Datetime(string='Time', readonly=True)

    def action_present(self):
        self.time = fields.Datetime.now()
        self.is_present = True
