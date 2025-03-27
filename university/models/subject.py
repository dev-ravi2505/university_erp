from odoo import fields, models


class SubjectInfo(models.Model):
    _name = "subject.info"
    _description = "Subject Information"
    _rec_name = "sub_name"

    code = fields.Char(string='Code')
    type = fields.Selection([
        ('compulsory' , 'Compulsory'),
        ('secondary' , 'Secondary'),
        ], default='compulsory', string='Type', required=True)
    language = fields.Boolean(string='Language')
    sub_name = fields.Char(string='Subject', required=True)
    weightage = fields.Float(string='Weightage', default=1.0)
    lab = fields.Boolean(string='Lab')
    description = fields.Text(string='Description')

