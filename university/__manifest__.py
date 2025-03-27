# -*- coding: utf-8 -*-
{
    # App information
    'name': 'University',
    'version': '17.0.0.1',
    'summary': 'ERP Module for University Management',
    'category': 'Custom/University Management',
    'author': 'Ravi Prajapati',
    'license': 'LGPL-3',

    # Dependencies
    'depends': ['mail', 'base', 'hr'],

    # Data
    'data': [
        'security/ir.model.access.csv',

        'data/ir_sequence.xml',

        'views/university_menuitem.xml',
        'views/student_application_views.xml',
        'views/course_views.xml',
        'views/department_views.xml',
        'views/semester_views.xml',
        'views/academic_year_views.xml',
        'views/document_views.xml',
        'views/student_info_views.xml',
        'views/faculty_info_views.xml',
        'views/subject_views.xml',
    ],

    # Images
    'images': [
    ],

    # Technical
    'installable': True,
    'application': True,
    'auto_install': False,
}
