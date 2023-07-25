# -*- coding: utf-8 -*-
from odoo import models, api, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    def name_get(self):
        orig_name = super(ResPartner, self).name_get()
        result = []
        print("NAME GET", orig_name)
        if self.env.context.get('origin') == 'sale_order':
            for record in self:
                product_info = self.env['product.supplierinfo'].search([
                    ('name', '=', record.id),
                    ('product_tmpl_id', '=', self.env.context.get('default_product'))
                ])
                print("RECORD", record.name, record.id, (self.env.context.get('default_product'))
 )
                print("PRODUCT_INFO", product_info.name , product_info.id, product_info.date_start)
                fecha_descuento = ''
                if(product_info.date_start):
                    print("DATE START")
                    fecha_descuento = product_info.date_start
                    print("DATOS:", fecha_descuento,record.name,product_info.price,product_info.discount)
                result.append((record.id, "%s %s %s %s" % (record.name, product_info.price, product_info.discount, fecha_descuento)))
            print("RESULT:", result)
            return result
        return orig_name

        # FUNCION QUE DETECTA QUE SE ACCEDE AL CAMPO Y APLICA UN DOMAIN EN FUNCION DE UN VALOR DEL FORMULARIO PADRE

    @api.model
    def name_search(self, name, args=None, operator='ilike', limit=100):
        if self.env.context.get('origin') == 'sale_order':
            proveedores = []
            pt = self.env['product.product'].search([('id', '=', self.env.context.get('default_product'))])
            proveedores = self.env['product.supplierinfo'].search([('product_tmpl_id', '=', pt.product_tmpl_id.id)])

            args = [
                ('id', 'in', proveedores.mapped('name').ids)
            ]
        return super(ResPartner, self).name_search(name, args, operator, limit)
