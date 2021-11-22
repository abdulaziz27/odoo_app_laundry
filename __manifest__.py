{
    'name': 'Laundry',
    'summary': """Management Jasa Laundry Kiloan""",
    'description': 'Modul ini berfungsi untuk memanage semua proses yang ada pada jasa laundry kiloan',
    'author': 'Muhammad Azis - 087881071515',
    'website': "https://www.tutorialopenerp.wordpress.com",
    'category': "Industries",
    'version': '12.1',
    'depends': ['base', 'mail', 'sale', 'account', 'uom'],
    'data': [
        'report/report_laundry_order.xml',
        'report/report_laundry_label.xml',
        'report/report_laundry_receipt.xml',
        'views/action_report.xml',
        'views/views.xml',
    ],
    'demo': [
        'data/data.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}