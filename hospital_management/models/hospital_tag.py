
# -*- coding: utf-8 -*-

from odoo import fields, api, models


class HospitalTag(models.Model):
    _name = 'hospital.tag'
    _description = 'Hospital Tag Registration data'

    name = fields.Char(string='Name', required=True)
    sequence = fields.Integer(string='Sequence', required=True)
