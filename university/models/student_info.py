from odoo import fields, models


class StudentInfo(models.Model):
    _name = "student.info"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Student Information"
    _rec_name = "first_name"

    admission_number = fields.Char(string='Admission Number', required=True, default=lambda self: 'New')
    application_id = fields.Many2one('student.application.info', string="Application Reference", required=True)

    first_name = fields.Char(string='First Name', required=True)
    middle_name = fields.Char(string='Middle Name')
    last_name = fields.Char(string='Last Name', required=True)
    batch_name = fields.Char(string='Batch', store=True, readonly=False)
    semester_info_id = fields.Many2one('semester.info', string='Semester', required=True)
    department_info_id = fields.Many2one('department.info', string='Department', required=True)
    course_info_id = fields.Many2one('course.info', string='Course', required=True, track_visibility='onchange')
    academic_year_info_id = fields.Many2one('academic.year.info', string='Academic Year', required=True)
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company)

    # STUDENT INFO
    father_name = fields.Char(string='Father', store=True, readonly=False)
    mother_name = fields.Char(string='Mother', store=True, readonly=False)
    guardian_name = fields.Char(string='Gaurdian', required=True, store=True, readonly=False)
    user_id = fields.Many2one('res.users', string='User')
    religion = fields.Char(string='Religion', store=True, readonly=False)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string='Gender')
    dob = fields.Date(string='Date of Birth', required=True, track_visibility='onchange')
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
    cast = fields.Char(string='Cast', store=True, readonly=False)
    nationality = fields.Char(string='Nationality', store=True, readonly=False)

    # CONTACT DETAIL
    email_name = fields.Char(string='Email', required=True, store=True, readonly=False)
    mobile_number = fields.Char(string='Mobile', required=True, store=True, readonly=False)
    phone_number = fields.Char(string='Phone', required=True, store=True, readonly=False)

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
