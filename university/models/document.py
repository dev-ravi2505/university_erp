from odoo import fields, models


class DocumentInfo(models.Model):
    _name = "document.info"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Document Information"
    _rec_name = "reference_number"

    reference_number = fields.Char(string='Reference number')
    document_type = fields.Char(string='Document Type')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('correction', 'Correction'),
        ('done', 'Done'),
    ], string='Application Status', readonly=True, default='draft', track_visibility='onchange')
    attachment_ids = fields.Many2many('ir.attachment', string='Attachment')
    student_application_info_id = fields.Many2one('student.application.info', string='Application Ref.')

    description = fields.Text(string='Description')
    user_id = fields.Many2one('res.users', string='User')
    date = fields.Date(string='Date')

    def action_verify(self):
        for record in self:
            record.write({
                'user_id': self.env.user.id,
                'date': fields.Datetime.now().strftime('%Y-%m-%d'),
                'state': 'done',
            })

    def action_correction(self):
        self.write({'state': 'correction'})
