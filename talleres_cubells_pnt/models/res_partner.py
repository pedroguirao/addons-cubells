# -*- coding: utf-8 -*-
from odoo import models, api, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    #@api.multi
    #def name_get(self):
    #    orig_name = super(ResPartner, self).name_get()
    #    result = []

    #    if self.env.context.get('origin') == 'sale_order':
    #        for record in self:
    #            product_info = self.env['product.supplierinfo'].search([
    #                ('name', '=', record.id),
    #                ('product_tmpl_id', '=', self.env.context.get('default_product'))
    #            ])
    #            fecha_descuento = ''
    #            if(product_info.date_start):
    #                fecha_descuento = product_info.date_start
    #            result.append((record.id, "%s %s %s %s" % (record.name, product_info.price, product_info.discount, fecha_descuento)))
    #        return result
    #    return orig_name

        # FUNCION QUE DETECTA QUE SE ACCEDE AL CAMPO Y APLICA UN DOMAIN EN FUNCION DE UN VALOR DEL FORMULARIO PADRE

    #@api.model
    #def name_search(self, name, args=None, operator='ilike', limit=100):
    #    if self.env.context.get('origin') == 'sale_order':
    #        proveedores = []
    #        pt = self.env['product.product'].search([('id', '=', self.env.context.get('default_product'))])
    #        proveedores = self.env['product.supplierinfo'].search([('product_tmpl_id', '=', pt.product_tmpl_id.id)])

    #        args = [
    #            ('id', 'in', proveedores.mapped('name').ids)
    #        ]
    #    return super(ResPartner, self).name_search(name, args, operator, limit)
