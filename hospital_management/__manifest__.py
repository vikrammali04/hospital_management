{
    "name": "Hospital Management Custom module",
    "version": "15.0.1",
    "author": "Silver Touch Technologies Limited",
    'category': 'Hospital Management',
    'sequence': -100,
    "website": "",
    "description": """
""",
    'depends': [],
    'data': [
        'views/menu.xml',
        'views/hospital_view.xml',
        'security/ir.model.access.csv',
        'views/tag_view.xml',
        'views/staff_view.xml',
        'views/staff_interview.xml',
        'security/security.xml',
        
        
    ],
    'installable': True,
    'application': True,
    'auto_install' : False,
    'demo' : [],
    'license': 'LGPL-3',
    'assets' : {}
}