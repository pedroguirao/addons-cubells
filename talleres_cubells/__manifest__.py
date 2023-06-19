# b-*- encoding: utf-8 -*-
##############################################################################
#
#    Copyright (c) 2017 brain-tec AG (http://www.braintec-group.com)
#    All Right Reserved
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    "name": "Talleres Rafael Cubells Ballester SL - Migracion de datos",
    "version": "11.0.1.0.0",
    "author": "brain-tec AG",
    "description": """Este módulo se utiliza para migrar los datos del sistema antiguo""",
    "category": "Custom/Import",
    "website": "http://www.braintec-group.com/",
    "depends": [
        "base",
#        "crm",
#        "sale",
#        "purchase",
#        "account",
#        "stock",
#        "account_accountant",
#        "l10n_es"
    ],
    "data": [
        # unfortunately CSV doesn't work with noupdate thus we use a post_init hook
        # 'data/plan_contable/account.account.csv',
        # 'data/proveedores/res.partner.csv',
        # 'data/clientes/res.partner.csv',
        # 'data/articulos/product.template.csv',

 #       'views/account_account_views.xml',
 #       'views/res_partner_views.xml',
 #       'views/product_template_views.xml',
    ],
    "demo": [
    ],
    "qweb": [
    ],
 #   'pre_init_hook': 'pre_init_hook',
 #   'post_init_hook': 'post_init_hook',
 #   'uninstall_hook': 'uninstall_hook',
    "active": False,
    "installable": True,
}
