from odoo import api, models, fields


# One customer can receive multiple unique promo codes over time.
# Each promo code belongs to only one customer and is still one-time use. => personal code

# if many customer has the same code and the customers only uses one code at time ==> many to one
class StorePromos(models.Model):
    _name = 'superstore.promos'  # Change to represent customers
    _inherit = ['mail.thread']
    _description = 'SuperStore Promos'
    _rec_name = 'customer_id'
    
    date_created = fields.Datetime(string="Date Created", default=fields.Datetime.now, readonly=True)
    promo_code = fields.Char(string='Code', default ='New')
    customer_id = fields.Many2one('superstore.customer', string='Customer')
    promo_description = fields.Char(string='Description')
    discount = fields.Char(string='Discount')
    state = fields.Selection(
        [('applied','Coupon Applied'), ('expired','Expired'),
         ('upcoming','Upcoming'),('ongoing','Ongoing')], default = 'ongoing', tracking=True
    )
    
    @api.model_create_multi # for like ID for the code
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('promo_code') or vals['promo_code'] == 'New':
                vals['promo_code'] = self.env['ir.sequence'].next_by_code('superstore.promos')
        return super().create(vals_list)
    
    # for me clickable option is more efficient
    # def action_ongoing(self):
    #     for rec in self:
    #         rec.self = 'ongoing'