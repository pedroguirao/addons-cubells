# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2018 Pablo Archanco Alonso - Aselcis Consulting (http://www.aselcis.com). All Rights Reserved
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################
from odoo import models, api


class AccountInvoice(models.Model):
    _inherit = 'account.move'

    #@api.multi
    #def action_invoice_open(self):
    #    res = super(AccountInvoice, self).action_invoice_open()
    #    if self.type in ['in_invoice', 'in_refund']:
    #        psi_obj = self.env['product.supplierinfo']
    #        for l in self.invoice_line_ids:
    #            psi = psi_obj.search(
    #                [('product_tmpl_id', '=', l.product_id.product_tmpl_id.id), ('name', '=', self.partner_id.id)],
    #                limit=1)
    #            if psi:
    #                psi.write({
    #                    'discount': l.discount,
    #                    'price': l.price_unit,
    #                    'date_start': self.date_invoice
    #                })
    #            else:
    #                psi_obj.create({
    #                    'name': self.partner_id.id,
    #                    'product_tmpl_id': l.product_id.product_tmpl_id.id,
    #                    'discount': l.discount,
    #                    'price': l.price_unit,
    #                    'date_start': self.date_invoice
    #                })
    #    return res
