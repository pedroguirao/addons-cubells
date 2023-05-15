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

from logging import getLogger
_logger = getLogger(__name__)


def pre_init_hook(cr):
    # Uninstall all the existent accounts
    cr.execute("UPDATE account_tax SET account_id=NULL, refund_account_id=NULL;")
    cr.execute("DELETE FROM account_fiscal_position_account;")
    cr.execute("DELETE FROM account_account;")


def post_init_hook(cr, registry):
    """Import CSV data because we can't use noupdate with csv"""
    from odoo.tools import convert_file

    files_to_import = [
        'data/plan_contable/account.account.type.csv',
        'data/plan_contable/account.account.csv',
        'data/proveedores/res.partner.csv',
        'data/clientes/res.partner.csv',
        'data/articulos/product.template.csv',
    ]

    for filename in files_to_import:
        _logger.info("post_init_hook -> Importing {0}".format(filename))
        convert_file(cr, 'talleres_cubells', filename, None, mode='init', noupdate=True,
                     kind='init', report=None)


def uninstall_hook(cr, registry):
    pass
