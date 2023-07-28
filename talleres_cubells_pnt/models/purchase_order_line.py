# -*- coding: utf-8 -*-
from odoo import models, api, fields

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    wo_num = fields.Char('WO Num')

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

