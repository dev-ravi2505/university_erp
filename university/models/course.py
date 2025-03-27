from odoo import fields, models


class CourseInfo(models.Model):
    _name = "course.info"
    _description = "Course Information"
    _rec_name = "name"

    name = fields.Char(string='Name')
    course_category = fields.Selection([
        ('diploma' , 'Diploma'),
        ('graduate' , 'Graduate'),
        ('post-graduate' , 'Post-Graduate'),
    ], string='Course Category', required=True)
    number_of_semester = fields.Integer(string='No of Semester', required=True)