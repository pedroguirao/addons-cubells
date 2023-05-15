from odoo import api, fields, models, _


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    partner_bank_acc_id = fields.Many2one(
        string="Partner bank account",
        comodel_name="res.partner.bank",
    )

    #@api.onchange("partner_id", "company_id")
    #def _onchange_partner_id(self):
    #    res = super()._onchange_partner_id()
    #    if self.partner_id:
    #        self.partner_bank_acc_id = self.env["res.partner.bank"].search([
    #            ("partner_id", "=", self.partner_id.id),
    #        ], limit=1)
    #    else:
    #        self.partner_bank_acc_id = False
    #    return res

    #def parser_bank_acc(self, bank_acc):
    #    if bank_acc.acc_number:
    #        return "XXXX XXXX XXXX XXXX " + bank_acc.acc_number[-4:]
    #    return ""
