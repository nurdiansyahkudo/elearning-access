# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class elearning_subscription_access(models.Model):
#     _name = 'elearning_subscription_access.elearning_subscription_access'
#     _description = 'elearning_subscription_access.elearning_subscription_access'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

