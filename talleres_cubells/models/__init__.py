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

from io import StringIO
import csv
import logging
import os.path

import odoo
import odoo.release
from odoo.tools.misc import file_open, unquote, ustr, SKIPPED_ELEMENT_TYPES
from odoo.tools.translate import _
from odoo import SUPERUSER_ID

_logger = logging.getLogger(__name__)

from . import account_account_ext
from . import res_partner_ext
from . import product_template_ext
