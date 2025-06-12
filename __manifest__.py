{
    'name': 'eLearning Subscription Access Control',
    'version': '1.0',
    'category': 'eLearning',
    'author': 'PT. Lintang Utama Infotek',
    'summary': 'Restrict eLearning course access based on subscription status',
    'depends': ['website_slides', 'sale_subscription', 'sale'],
    'data': [
      "views/website_slides_templates_course_inherit.xml",
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
