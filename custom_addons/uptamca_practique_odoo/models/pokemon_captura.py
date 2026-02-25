import requests
from odoo import models, fields, api, _
from odoo.exceptions import UserError

class CapturaPokemon(models.Model):
    _name = 'captura.pokemon'
    _description = 'Captura de Pokémones'

    name = fields.Char(string='Nombre', required=True)
    
    pokemon_id = fields.Many2one(
        comodel_name='pokemon',
        string='Pokemon',
        required=True,
        tracking=True,
        help='Pokemon capturar')
    
        