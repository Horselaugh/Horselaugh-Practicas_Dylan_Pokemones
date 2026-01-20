from odoo import models, fields, api
import requests
import logging

_logger = logging.getLogger(__name__)

class Pokemon(models.Model):
    _name = 'pokemon.pokemon'
    _description = 'Pokémon'
    
    name = fields.Char(string='Nombre', required=True)
    pokedex_number = fields.Integer(string='N° Pokédex', required=True)
    category = fields.Char(string='Tipo')
    
    # Relación con entrenadores
    entrenador_ids = fields.Many2many(
        'pokemon.entrenador',
        string='Capturado por'
    )
    
    # Campos adicionales de la API
    abilities = fields.Char(string='Habilidades')
    height = fields.Float(string='Altura (m)')
    weight = fields.Float(string='Peso (kg)')
    
    @api.model
    def cargar_pokemon_desde_api(self):
        """Carga los primeros 151 Pokémon desde la API"""
        url = "https://pokeapi.co/api/v2/pokemon?limit=10"  # Solo 10 para prueba
        
        try:
            response = requests.get(url, timeout=10)
            data = response.json()
            
            for pokemon_data in data['results']:
                # Obtener detalles
                detail_response = requests.get(pokemon_data['url'], timeout=10)
                detail = detail_response.json()
                
                # Crear Pokémon
                vals = {
                    'name': pokemon_data['name'].capitalize(),
                    'pokedex_number': detail['id'],
                    'category': ', '.join([t['type']['name'] for t in detail['types']]),
                    'abilities': ', '.join([a['ability']['name'] for a in detail['abilities']]),
                    'height': detail['height'] / 10,
                    'weight': detail['weight'] / 10,
                }
                
                # Crear si no existe
                if not self.search([('pokedex_number', '=', detail['id'])]):
                    self.create(vals)
                    _logger.info(f"Pokémon creado: {pokemon_data['name']}")
                    
        except Exception as e:
            _logger.error(f"Error: {e}")