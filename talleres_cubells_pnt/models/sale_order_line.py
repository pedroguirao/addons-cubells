
from odoo import models, api, fields
from datetime import timedelta


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    section = fields.Integer('Section', store=True)
    seller_ids = fields.Many2one(
        comodel_name="res.partner",
        string='Proveedor'
    )

    product_cost_price = fields.Float(string='Precio Coste')
    product_net_cost_price = fields.Float(string='Precio Coste Neto',
                                          default=0.0)
    product_discount_seller = fields.Float(string='Descuento Proveedor')
    product_margin_price = fields.Float(string='Margen')


    @api.onchange('product_id')
    def _get_name_printed(self):
        for record in self:
            nombre = record.name
            if record.product_id.default_code:
                printedcode = "[" + record.product_id.default_code + "]"
                largocode = len(printedcode)
                orden = record.name.find(printedcode)
                fincodigo = orden + largocode
                nombre = (record.name[:orden] + record.name[fincodigo:])
            record['name_printed'] = nombre
    name_printed = fields.Char('Name printed', store=False, compute='_get_name_printed')


    #@api.onchange('product_id')
    #def _onchange_product_id(self):
    ##    print("ONCHANGE")
    #    if self.product_id:
    #        self.seller_ids = ''
    #        domain_seller = [
    #            ('id', 'in', self.product_id.seller_ids.ids)]
    #        return {'domain': {'seller_ids': domain_seller}}

    @api.onchange('seller_ids')
    def _onchange_seller_ids(self):
        discount_seller = 0
        product_price = self.env['product.supplierinfo'].search(
            [
                ('product_tmpl_id', '=', self.product_id.product_tmpl_id.id),
                ('partner_id', '=', self.seller_ids.id),
                ('date_start', '<=', fields.Datetime.now()),
                '|',
                ('date_end', '>=', fields.Datetime.now()),
                ('date_end', '=', False),
            ]
        )

        self.product_cost_price = product_price.price
        self.product_discount_seller = product_price.discount
        discount_seller = self.product_cost_price * (
                product_price.discount / 100)
        self.product_net_cost_price = self.product_cost_price - discount_seller

        self.price_unit = self.product_net_cost_price
        if self.product_margin_price > 0:
            self.calcula_coste_product()

    @api.onchange('product_margin_price')
    def _onchange_product_margin_price(self):
        if self.seller_ids:
            self.calcula_coste_product()

    def calcula_coste_product(self):
        margin = self.product_net_cost_price * (self.product_margin_price / 100)
        self.price_unit = self.product_net_cost_price + margin

