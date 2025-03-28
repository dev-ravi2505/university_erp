from os import WCONTINUED

from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class StudentApplicationInfo(models.Model):
    _name = "student.application.info"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Student Application Information"
    _rec_name = "application_number"

    application_number = fields.Char(string='Application Number', required=True, default=lambda self: 'New',
                                     readonly=True)
    first_name = fields.Char(string='First Name', required=True)
    middle_name = fields.Char(string='Middle Name')
    last_name = fields.Char(string='Last Name', required=True)
    academic_year_info_id = fields.Many2one('academic.year.info', string='Academic Year', required=True)
    date = fields.Date(string='Admission Date')
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company)
    course_info_id = fields.Many2one('course.info', string='Course', required=True, track_visibility='onchange')
    department_info_id = fields.Many2one('department.info', string='Department', required=True)
    semester_info_id = fields.Many2one('semester.info', string='Semester', required=True)
    batch_info_id = fields.Many2one('batch.info', string='Batch', required=True)

    state = fields.Selection([
        ('draft', 'Draft'),
        ('verify', 'Verify'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('done', 'Done'),
        ('cancel', 'Cancel'),
    ], string='Application Status', readonly=True, default='draft', track_visibility='onchange')

    # Personal Details Fields
    dob = fields.Date(string='Date of Birth', required=True, track_visibility='onchange')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string='Gender')
    father_name = fields.Char(string='Father')
    mother_name = fields.Char(string='Mother')
    guardian_name = fields.Char(string='Gaurdian', required=True)
    blood_group = fields.Selection([
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
    ], default='O+', string='Blood Group')
    nationality = fields.Char(string='Nationality')
    mother_tongue = fields.Char(string='Mother Tongue')
    religion = fields.Char(string='Religion')
    cast = fields.Char(string='Cast')

    # CONTACT DETAILS
    email_name = fields.Char(string='Email', required=True)
    mobile_number = fields.Char(string='Mobile', required=True)
    phone_number = fields.Char(string='Phone', required=True)

    # CONTACT ADDRESS DETAILS
    street = fields.Char(required=True)
    street2 = fields.Char()
    zip = fields.Char()
    city = fields.Char()
    state_id = fields.Many2one("res.country.state", string='State', ondelete='restrict',
                               domain="[('country_id', '=?', country_id)]")
    country_id = fields.Many2one('res.country', string='Country', ondelete='restrict')

    is_same_as_permanent_address = fields.Boolean(string='As Same as Permanent Address')

    current_street = fields.Char()
    current_street2 = fields.Char()
    current_zip = fields.Char()
    current_city = fields.Char()
    current_state_id = fields.Many2one("res.country.state", string='State', ondelete='restrict',
                                       domain="[('country_id', '=?', country_id)]")
    current_country_id = fields.Many2one('res.country', string='Country', ondelete='restrict')
    image = fields.Image("Image")
    document_count = fields.Integer(compute='_compute_document_count')

    def action_reject(self):
        """Method to set application state as 'Rejected'"""
        for rec in self:
            rec.state = 'rejected'

    def action_approve(self):
        """Method to set application state as 'Approved'"""
        for rec in self:
            document_id = self.env['document.info'].search([('student_application_info_id', '=', rec.id)])
            for document in document_id:
                if not (document.state == "done"):
                    raise ValidationError('Document are not verified yet!!!')
                else:
                    rec.write({'state': 'approved'})

    def send_for_verification(self):
        for rec in self:
            document_id = self.env['document.info'].search([('student_application_info_id', '=', rec.id)])
            if not document_id:
                raise ValidationError(_('No Document Found.'))
            else:
                rec.write({'state': 'verify'})

    def _compute_document_count(self):
        for record in self:
            record.document_count = self.env['document.info'].search_count(
                [('student_application_info_id', '=', record.id)]
            )

    def redirect_student_document(self):
        return {
            'name': 'Documents',
            'view_mode': 'tree,form',
            'res_model': 'document.info',
            'domain': [('student_application_info_id', '=', self.id)],
            'view_id': False,
            'type': 'ir.actions.act_window',
            'context': {'default_student_application_info_id': self.id}
        }

    @api.model_create_multi
    def create(self, vals_list):
        for record in vals_list:
            if record.get('application_number', _('New')) == _('New'):
                record['application_number'] = self.env['ir.sequence'].next_by_code('student_application_number') or _(
                    'New')
        return super().create(vals_list)

    def action_create_student(self):
        self.ensure_one()
        vals = {
            'admission_number': self.application_number,
            'first_name': self.first_name,
            'middle_name': self.middle_name,
            'last_name': self.last_name,
            'batch_name': self.batch_name,
            'semester_info_id': self.semester_info_id.id,
            'department_info_id': self.department_info_id.id,
            'course_info_id': self.course_info_id.id,
            'academic_year_info_id': self.academic_year_info_id.id,
            'company_id': self.company_id.id,
            'father_name': self.father_name,
            'mother_name': self.mother_name,
            'guardian_name': self.guardian_name,
            'religion': self.religion,
            'gender': self.gender,
            'dob': self.dob,
            'blood_group': self.blood_group,
            'cast': self.cast,
            'nationality': self.nationality,
            'email_name': self.email_name,
            'mobile_number': self.mobile_number,
            'phone_number': self.phone_number,
            'street': self.street,
            'street2': self.street2,
            'zip': self.zip,
            'city': self.city,
            'state_id': self.state_id.id,
            'country_id': self.country_id.id,
            'is_same_as_permanent_address': self.is_same_as_permanent_address,
            'image': self.image,
            'application_id': self.id,
        }
        if not self.is_same_as_permanent_address:
            vals.update({
                'current_street': self.current_street,
            })
        student = self.env['student.info'].create(vals)
        user_vals = {
            'name': self.first_name,
            'login': self.email_name,
            'password': self.email_name
        }
        student.user_id = self.env['res.users'].create(user_vals)
        self.write({
            'state': 'done'
        })
        return {
            'name': _('Student'),
            'view_mode': 'form',
            'res_model': 'student.info',
            'res_id': student.id,
            'context': self.env.context,
            'type': 'ir.actions.act_window',
            'view_id': self.env.ref('university.student_info_form_view').id,
        }
