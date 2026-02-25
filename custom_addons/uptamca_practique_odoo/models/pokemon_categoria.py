from odoo import models, fields, api

class Category(models.Model):
    _name = 'pokemon.category'
    _description = 'Categoría de Pokémon'

    name = fields.Char(string='Nombre de la Categoría', required=True, tracking=True)
    type = fields.Selection([
        ('pokemon', 'Pokémon'),
        ('trainer', 'Entrenador')
    ], string='Tipo', required=True, tracking=True, default='pokemon')