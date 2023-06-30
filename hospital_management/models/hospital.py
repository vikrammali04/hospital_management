# -*- coding: utf-8 -*-

from odoo import fields, api, models


class Hospital(models.Model):
    _name = 'res.hospital'
    _description = 'Hospital Registration data'
    _rec_name = 'hospital_name'

    hospital_name = fields.Char(string='Name', required=True)
    contact = fields.Char(string='Contact', size=10)
    street = fields.Char(string='Address')
    street2 = fields.Char(string='Address')
    city = fields.Char(string='City')
    pincode = fields.Char(string='Pin Code', required=True)
    partner_id = fields.Many2one('res.partner', string='Partner')
    tag_ids = fields.Many2many('hospital.tag', string='Tags')
    staff_ids = fields.One2many(
        'hospital.staff.members', 'hospital_id', string='Staff', required=True)
    sequence_count = fields.Integer(string='Sequqence Count')

    @api.model
    def create(self, vals):
        res = super(Hospital, self).create(vals)
        res.sequence_count = sum(res.tag_ids.mapped('sequence'))
        return res

    def write(self, vals):
        res = super(Hospital, self).write(vals)
        if vals.get('tag_ids'):
            self.sequence_count = sum(self.tag_ids.mapped('sequence'))
        return res

    def filter_by_partner(self):
        data = self.search([])
        hospital_names = data.filtered(
            lambda x: not x.partner_id).mapped('hospital_name')
        print('Hospitals without partners:', hospital_names)
        print('Sorted hospitals without partners:', sorted(hospital_names))
        print('num of hospitals in Ahmedabad: ',
              self.search_count([('city', '=', 'Ahmedabad')]))
        delet_rec = self.search([('hospital_name', '=', 'LD')])
        delet_rec.unlink()
        # print(self.env.ref('res.hospital'))


class HospitalStaffMembers(models.Model):
    _name = 'hospital.staff.members'
    _description = 'Hospital Staff Members'
    _rec_name = 'ref_id'

    ref_id = fields.Many2one('hospital.staff')
    age = fields.Integer(string="Age", related='ref_id.age', readonly=True)
    designation = fields.Char(string="Designantion",
                              related='ref_id.designation', readonly=True)
    hospital_id = fields.Many2one('res.hospital', string='Hospital')
