from odoo import models, fields

class ResUsers(models.Model):
    _inherit = 'res.users'

    custom_checkbox = fields.Boolean(string="Invoice Double Approval(Customer/Vendor Specific)")