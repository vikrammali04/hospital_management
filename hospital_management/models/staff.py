
# -*- coding: utf-8 -*-

from odoo import fields, api, models


class HospitalStaff(models.Model):
    _name = 'hospital.staff'
    _description = 'Hospital Staff data'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age', required=True)
    designation = fields.Char(string='Designation', required=True)
    img = fields.Image()


class StaffInterview(models.Model):
    _name = 'interview.staff'
    _description = 'Hospital Staff data'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    designation = fields.Char(string='Designation', required=True)
    interview_date = fields.Date(string='Interview Date', required=True)
    final_selection = fields.Boolean(default=False)
    img = fields.Image()

    @api.onchange('final_selection')
    def _onchange_interview_date(self):
        if self.final_selection:
            self.env['hospital.staff'].create({
                'name': self.name,
                'age': self.age,
                'designation': self.designation,
                'img': self.img,
            })
