# -*- coding: utf-8 -*-
from odoo import models, api, fields
from datetime import timedelta


class AccountInvoice(models.Model):
    _inherit = 'account.move'

    pnt_collaborator_id = fields.Many2one(
        comodel_name="res.partner",
        string='Collaborator',
        domain="[('is_company','=',1)]",
    )

    @api.onchange('product_id')
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

    #@api.model
    #def create(self, vals):
    #    res = super(AccountInvoice, self).create(vals)
    #    return res

