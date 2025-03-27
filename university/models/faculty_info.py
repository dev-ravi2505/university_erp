from odoo import fields, models, api, _


class FacultyInfo(models.Model):
    _name = "faculty.info"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Faculty Information"
    _rec_name = "first_name"

    # PERSNOL DETAILS

    first_name = fields.Char(string='First Name', required=True)
    last_name = fields.Char(string='Last Name', required=True)
    father_name = fields.Char(string='Father')
    mother_name = fields.Char(string='Mother')
    guardian_name = fields.Char(string='Guardian', required=True)
    degree = fields.Char(string='Degree')
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
    ], default='A+', string='Blood Group')

    # MANY2MANY FIELD
    subject_ids = fields.Many2many('subject.info', string='Subjects')

    # CONTACT DETAILS

    email_name = fields.Char(string='Email', required=True)
    mobile_number = fields.Char(string='Mobile', required=True)
    phone_number = fields.Char(string='Phone', required=True)

    image = fields.Image("Image")

    employee_id = fields.Many2one('hr.employee', string='Related Employee', readonly='1')

    def action_create_employee(self):
        """Creates an Employee Record from Faculty Info"""
        self.ensure_one()  # Ensures only one record is processed at a time

        employee_vals = {
            'name': f"{self.first_name} {self.last_name}",  # hr.employee expects 'name'
            'work_email': self.email_name,
            'mobile_phone': self.mobile_number,
            'work_phone': self.phone_number,
            'birthday': self.dob,  # 'birthday' instead of 'dob'
            'gender': self.gender,  # Odoo might not support gender in hr.employee
            'image_1920': self.image,  # hr.employee uses 'image_1920' for images
        }

        employee = self.env['hr.employee'].create(employee_vals)  # Creating employee
        self.employee_id = employee.id

        return {
            'type': 'ir.actions.act_window',
            'res_model': 'hr.employee',
            'view_mode': 'form',
            'res_id': employee.id,  # Fixing the reference to employee.id
            'target': 'current',
        }
