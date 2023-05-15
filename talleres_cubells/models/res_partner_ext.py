# b-*- encoding: utf-8 -*-
##############################################################################
#
#    Copyright (c) 2017 brain-tec AG (http://www.braintec-group.com)
#    All Right Reserved
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from odoo import api, fields, models


class ResPartnerExt(models.Model):
    _inherit = 'res.partner'

    # Campos requeridos por los proveedores
    sigla_nacion = fields.Char("Sigla Nacion")
    cif_dni = fields.Char("CIF/DNI")
    nombre1 = fields.Char("Nombre 1")
    codigo_divisa = fields.Char("Codigo divisa")
    actividad = fields.Char("Actividad")
    cargo = fields.Char("Cargo")
    codigo_definicion = fields.Char("Codigo Definicion")
    codigo_condiciones = fields.Char("Codigo Condiciones")
    forma_de_pago = fields.Char("Forma de pago (Importada)")
    codigo_banco = fields.Char("Codigo Banco")
    codigo_agencia = fields.Char("Codigo Agencia")
    dc = fields.Char("DC")
    ccc = fields.Char("CCC")
    iban = fields.Char("IBAN")
    telefono2 = fields.Char("Telefono 2")
    telefono3 = fields.Char("Telefono 3")

    # Campos requeridos por los clientes
    codigo_sigla = fields.Char("Codigo Sigla")
    numero1 = fields.Char("Numero 1")

    @api.constrains("vat")
    def check_vat(self):
        # Removing VAT check
        pass
