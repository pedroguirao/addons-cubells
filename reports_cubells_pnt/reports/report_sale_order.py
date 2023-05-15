from odoo import models, api

class SaleReport(models.AbstractModel):
    _name = "report.reports_cubells_pnt.report_saleorder"

    @api.multi
    def render_html(self, data=None):

        return super(SaleReport, self).render_html()

