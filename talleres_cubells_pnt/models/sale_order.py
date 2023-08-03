from odoo import models, api, fields
from datetime import timedelta


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    pnt_collaborator_id = fields.Many2one(
        comodel_name="res.partner",
        string='Collaborator',
        domain="[('is_company','=',1)]",
    )

    def pnt_sort_order_line(self):
        all_line_ids = self.order_line.sorted(key=lambda r: r.sequence)
        i, section = 1, 0
        # Asignar sección a todas las líneas:
        for li in all_line_ids:
            if li.display_type == 'line_section': section = li.id
            li.write({'sequence': i, 'section': section})
            i += 1
        # Ordenar alfabéticamente por sección:
        line_alphabetic_ids = self.order_line.sorted(key=lambda r: (r.section, r.name))
        for li in line_alphabetic_ids:
            li['sequence'] = i
            i += 1

    def calc_price_sale_order(self):
        discount_seller = 0

        order_lines = self.env['sale.order.line'].search([('order_id', '=', self.id),('display_type','=',False)])

        for record in order_lines:

            product_price = self.env['product.supplierinfo'].search(
                [
                    ('product_tmpl_id', '=', record.product_id.product_tmpl_id.id),
                    ('partner_id', '=', record.seller_ids.id),
                    ('date_start', '<=', fields.Datetime.now()),
                    '|',
                    ('date_end', '>=', fields.Datetime.now()),
                    ('date_end', '=', False),
                ], limit=1
            )
            if product_price:
                record.product_cost_price = product_price.price
                record.product_discount_seller = product_price.discount

                discount_seller = record.product_cost_price * (product_price.discount / 100)
                record.product_net_cost_price = record.product_cost_price - discount_seller
                record.price_unit = record.product_net_cost_price

                if record.product_margin_price > 0:
                    record.calcula_coste_product()

                margin = record.product_net_cost_price * (record.product_margin_price / 100)
                record.price_unit = record.product_net_cost_price + margin





    def order_lines_layouted(self):
        return True
    #    report_pages = super(SaleOrder, self).order_lines_layouted()
    #    new_pages = []
    #    cont = 0
    #    for pages in report_pages:
    #        for section in pages:
    #            pages[cont]['lines'] = sorted(section['lines'],
    #                                          key=lambda r: r.name)
    #            cont += 1
    #        new_pages.append(pages)
    #    return new_pages

    def picking_lines_layouted(self):
        return True
    #    report_pages = super(SaleOrder, self).order_lines_layouted()
    #    new_pages = []
    #    cont = 0
    #    for pages in report_pages:
    #        for section in pages:
    #            pages[cont]['lines'] = sorted(section['lines'],
    #                                          key=lambda r: r.sequence)
    #            cont += 1
    #        new_pages.append(pages)
    #    return new_pages
