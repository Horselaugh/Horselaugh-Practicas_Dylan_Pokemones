from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class Entrenador(models.Model):
    _name = 'pokemon.entrenador'
    _description = 'Entrenador Pokémon'
    
    name = fields.Char(string='Nombre', required=True)
    category = fields.Selection([
        ('novato', 'Novato'),
        ('medio', 'Entrenador Medio'),
        ('experto', 'Experto'),
        ('maestro', 'Maestro Pokémon'),
    ], string='Categoría', default='novato')
    
    # Relación con Pokémon capturados
    pokemon_ids = fields.Many2many(
        'pokemon.pokemon',
        string='Pokémon Capturados'
    )
    
    # Contador
    pokemon_count = fields.Integer(
        string='Total Capturados',
        compute='_compute_pokemon_count',
        store=True
    )
    
    @api.depends('pokemon_ids')
    def _compute_pokemon_count(self):
        for entrenador in self:
            entrenador.pokemon_count = len(entrenador.pokemon_ids)