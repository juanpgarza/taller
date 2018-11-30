# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = ['res.partner']

    tipo_recurso = fields.Selection([(1, 'Recurso Interno'), (2, 'Recurso Externo'), (3, 'No aplica')],
                        string='Recurso', default=2)
