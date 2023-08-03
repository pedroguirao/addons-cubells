# -*- coding: utf-8 -*-
from odoo import models, api, fields

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    wo_num = fields.Char('WO Num')

    def _get_name_printed(self):
        for record in self:
            name_printed = record.name
            if record.product_id.default_code:
                printedcode = "[" + record.product_id.default_code + "]"
                lencode = len(printedcode)
                position_start = record.name.find(printedcode)
                position_end = position_start + lencode
                name_printed = (record.name[:position_start] + record.name[position_end:])
            record['name_printed'] = name_printed
    name_printed = fields.Char('Name printed', store=False, compute='_get_name_printed')


    #@api.onchange('product_id')
    #def onchange_product_id(self):
    #    res = super(PurchaseOrderLine, self).onchange_product_id()

    #    if self.product_id.product_tmpl_id.id and self.partner_id.id:
    #        product_name_seller = self.env["product.supplierinfo"].search([
    #            ('product_tmpl_id', '=', self.product_id.product_tmpl_id.id),
    #            ('name', '=', self.partner_id.id)
    #        ])

    #        for product in product_name_seller:
    #            if product_name_seller:
    #                self.name = product.product_name
    #    return res

