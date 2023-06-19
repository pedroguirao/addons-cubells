# -*- coding: utf-8 -*-
{
    'name': 'Informes personalizados para Talleres Cubells',
    'version': '10.0.1.0.0',
    'summary': 'Informes',
    'author': 'Punt Sistemes S.L.U.',
    'contributors': ['Isaac Gallart <igallart@puntsistemes.es>'],
    'website': 'http://www.puntsistemes.es',
    'license': 'AGPL-3',
    'category': 'Report',
    'installable': True,
    'auto_install': False,
    'application': False,
    'depends': ['account_payment_partner',
                'delivery',
                'talleres_cubells_pnt'],
    'data': [
        #'reports/templates.xml',
        #        'reports/report_stock_view.xml',
        #'reports/report_delivery_view.xml',
        # 'reports/report_account_view.xml', (este ya estaba comentado antes de la migración)
        #'reports/report_sale_order.xml',
        #'reports/report_picking.xml',
        #'reports/report_purchase_view.xml',
        #'reports/report_purchase_unrated_view.xml'
    ]
}
