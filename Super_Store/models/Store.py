from odoo import api, models, fields

class StoreCustomer(models.Model):
    _name = 'superstore.customer'  # Change to represent customers
    _description = 'Superstore Customer'

    name = fields.Char(string="Customer Name", required=True)
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone Number")
    gender = fields.Selection([("male", 'Male'), ("female", 'Female')], string="Gender")
    birth_date = fields.Date(string="Date of Birth")
    address = fields.Text(string="Address")
    loyalty_points = fields.Integer(string="Loyalty Points", default=0)  # Example of a customer-related field
