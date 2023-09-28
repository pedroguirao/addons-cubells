# -*- coding: utf-8 -*-
from odoo import models, api, fields
from datetime import timedelta


class AccountInvoiceLine(models.Model):
    _inherit = 'account.move.line'

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


    @api.depends("product_id")
    def _compute_name(self):
        super()._compute_name()
        for line in self:
            if line.product_id:
                line.name = line.product_id.description_sale

