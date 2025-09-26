# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class membership_mass_invoicing(models.Model):
#     _name = 'membership_mass_invoicing.membership_mass_invoicing'
#     _description = 'membership_mass_invoicing.membership_mass_invoicing'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
