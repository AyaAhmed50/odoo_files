from odoo import api, models, fields

class StoreCustomer(models.Model):
    _name = 'superstore.customer'  # Change to represent customers
    _inherit = ['mail.thread']
    _description = 'Superstore Customer'
    
    name = fields.Char(
        string="Customer Name",
        required=True, tracking=True
                       )
    email = fields.Char(
        string="Email",
        tracking=True,
        )
    phone = fields.Char(
        string="Phone Number",
        tracking=True,
        )
    gender = fields.Selection(
        [("male", 'Male'), ("female", 'Female')],
        string="Gender",
        tracking=True,
        )
    birth_date = fields.Date(
        string="Date of Birth",
        tracking=True,
        )
    address = fields.Text(
        string="Address",
        tracking=True,
        )
    loyalty_points = fields.Integer(
        string="Loyalty Points",
        default=0,
        tracking=True,
        )  # Example of a customer-related field
