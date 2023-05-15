from odoo import api, fields, models, _


class AccountJournal(models.Model):
    _inherit = "account.journal"

    pnt_display_on_footer = fields.Boolean(
        string="Show in Invoices Footer",
        help="Display this bank account on the footer of printed documents "
             "like invoices and sales orders."
    )
