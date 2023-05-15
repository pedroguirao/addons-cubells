from dateutil import parser
from odoo import api, fields, models, _


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    parent_id = fields.Many2one(
        string="Contact",
        comodel_name="res.partner",
    )
    creator_id = fields.Many2one(
        string="Created by",
        comodel_name="res.users",
    )

    #@api.model
    #def create(self, vals):
    #    vals['creator_id'] = self._uid
    #    return super(PurchaseOrder, self).create(vals)

    #def datetime_to_date(self, date):
    #    return parser.parse(date).date().strftime("%d-%m-%Y")
