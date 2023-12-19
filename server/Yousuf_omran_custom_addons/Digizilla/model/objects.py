from odoo import api, models, fields

class objects(models.Model):
    _name = 'digizilla.objects'
    _inherit= 'mail.thread'
    _description= 'Employee Records'


    Name= fields.Char(string='Name', required=True, tracking=True)
    Gender= fields.Selection([('male','Male'), ('female','Female')], string='Gender', tracking=True)
    Country= fields.Many2one('res.country', string='Country', tracking=True)
    Joining_Date= fields.Date(string='Joining Date', tracking=True)
    Tags= fields.Char(string='Tags', tracking=True)
    Customers= fields.Many2many('res.partner', string='Customers', tracking=True)
    Company= fields.Many2one('res.company', string='Company', required=True, tracking=True)
    Notes= fields.Text(string='Notes', tracking=True)
    Comments= fields.Char(string='Comments', tracking=True)
    