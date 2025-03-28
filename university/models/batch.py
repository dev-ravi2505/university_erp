from odoo import fields, models, api


class BatchInfo(models.Model):
    _name = "batch.info"
    _description = "Batch Information"
    _rec_name = "name"

    @api.model
    def create(self, vals):
        res = super(BatchInfo, self).create(vals)
        semester_id = self.env['semester.info'].browse(
            vals['semester_info_id'])
        academic_year_id = self.env['academic.year.info'].browse(
            vals['academic_year_info_id'])
        name = str(semester_id.name + ' / ' + academic_year_id.name)
        res.name = name
        return res

    name = fields.Char(string='Name', readonly=True, default=lambda self: 'New')
    semester_info_id = fields.Many2one('semester.info', string='Semester', required=True)
    academic_year_info_id = fields.Many2one('academic.year.info', string='Academic Year', required=True)
    faculty_info_id = fields.Many2one('faculty.info', string='Faculty', required=True)
    department_info_id = fields.Many2one('department.info', string='Department',
                                         related='semester_info_id.department_info_id')
    batch_strength = fields.Char(string='Batch Strength')
