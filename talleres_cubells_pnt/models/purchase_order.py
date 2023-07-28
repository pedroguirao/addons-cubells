# -*- coding: utf-8 -*-
from odoo import models, api, fields

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'


    date_order_pnt = fields.Datetime('Fecha pedido', related='date_order', store=True)
