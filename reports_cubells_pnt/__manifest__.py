# -*- coding: utf-8 -*-
{
    'name': 'Informes personalizados para Talleres Cubells',
    'version': '16.0.0.0.0',
    'summary': 'Informes',
    'author': 'Punt Sistemes S.L.U.',
    'contributors': ['Javier Muñoz <jmunoz@puntsistemes.es>'],
    'website': 'http://www.puntsistemes.es',
    'license': 'AGPL-3',
    'category': 'Report',
    'installable': True,
    'auto_install': False,
    'application': False,
    'depends': [
                'sale_management',
                'account',
                'purchase',
                'stock',
                'talleres_cubells_pnt',
                ],
    'data': [
        'reports/report_purchaseorder_document.xml',
        'reports/report_picking.xml',
        'reports/report_purchasequotation_document.xml',
        'reports/report_delivery_document.xml',
        'reports/report_saleorder_document.xml',
        'reports/report_invoice_document.xml',
        'reports/report_saleorder_unvalued_document.xml',
    ]
}
