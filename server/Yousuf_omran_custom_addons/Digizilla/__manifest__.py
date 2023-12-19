
{
    'name': 'Digizilla',
    'version': '1.0',
    'license': 'LGPL-3',
    'summary': 'Tecknical Assessment',
    'description': 'Longer module description',
    'category': 'IT Solutions',
    'author': 'Yousuf Mohsen Omran',
    'website': 'https://www.digizilla.net',
    'depends': ['base', 'mail', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/objects.xml',
        'reports/report_digizilla_template.xml',
        'reports/report_digizilla.xml',
    ],
    'qweb':[],
    'installable': True,
    'auto_install': False,
    'application': True,
}
