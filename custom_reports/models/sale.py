from odoo import api, fields, models, _


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    #@api.onchange('product_id')
    #def product_id_change(self):
    #    res = super().product_id_change()
    #    self.name = self.product_id.description_sale
    #    return res
