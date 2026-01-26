from odoo import models, fields, api
import requests
import logging

_logger = logging.getLogger(__name__)

class Pokemon(models.Model):
    _name = 'pokemon.pokemon'
    _description = 'Pokémon'
    
    # Campos para la información general de la API
    name = fields.Char(string='Nombre', required=True)
    pokedex_number = fields.Integer(string='N° Pokédex', required=True)
    category = fields.Char(string='Categoría')
    url_info = fields.Char(string='URL de Información')
    
    # Campos para la información detallada de la API
    height = fields.Float(string='Altura (decímetros)')
    weight = fields.Float(string='Peso (hectogramos)')
    base_experience = fields.Integer(string='Experiencia Base')
    
    # Tipos 
    types = fields.Char(string='Tipos')
    
    # Habilidades
    abilities = fields.Text(string='Habilidades')
    
    # Estadísticas base
    hp = fields.Integer(string='HP')
    attack = fields.Integer(string='Ataque')
    defense = fields.Integer(string='Defensa')
    special_attack = fields.Integer(string='Ataque Especial')
    special_defense = fields.Integer(string='Defensa Especial')
    speed = fields.Integer(string='Velocidad')
    
    # URL de la imagen
    image_url = fields.Char(string='URL de Imagen')
    
    # Relación con entrenadores
    entrenador_ids = fields.Many2many(
        'pokemon.entrenador',
        string='Capturado por'
    )
    
    @api.model
    def cargar_pokemon_desde_api_lista(self):
        url = "https://pokeapi.co/api/v2/pokemon?"  
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
                }
                
                # Crear si no existe
                if not self.search([('pokedex_number', '=', detail['id'])]):
                    self.create(vals)
                    _logger.info(f"Pokémon creado: {pokemon_data['name']}")
                    
        except Exception as e:
            _logger.error(f"Error: {e}")

    @api.model
    def cargar_pokemon_desde_api(self):
        for i in range(1, 154):
            url = f"https://pokeapi.co/api/v2/pokemon/{i}/"
            try:
                response = requests.get(url, timeout=10)
                response.raise_for_status()
                data = response.json()
                
                # Extraer tipos
                types_list = [t['type']['name'] for t in data.get('types', [])]
                
                # Extraer habilidades
                abilities_list = [a['ability']['name'] for a in data.get('abilities', [])]
                
                # Extraer estadísticas
                stats = {}
                for stat in data.get('stats', []):
                    stat_name = stat['stat']['name']
                    stats[stat_name] = stat['base_stat']
                
                # URL de imagen (front_default)
                image_url = data.get('sprites', {}).get('front_default', '')
                
                # Crear Pokémon con todos los datos
                vals = {
                    'name': data['name'].capitalize(),
                    'pokedex_number': data['id'],
                    'url_info': url,
                    'height': data.get('height', 0),
                    'weight': data.get('weight', 0),
                    'base_experience': data.get('base_experience', 0),
                    'types': ', '.join(types_list),
                    'abilities': ', '.join(abilities_list),
                    'hp': stats.get('hp', 0),
                    'attack': stats.get('attack', 0),
                    'defense': stats.get('defense', 0),
                    'special_attack': stats.get('special-attack', 0),
                    'special_defense': stats.get('special-defense', 0),
                    'speed': stats.get('speed', 0),
                    'image_url': image_url,
                }
                
                # Buscar si ya existe
                pokemon_existente = self.search([('pokedex_number', '=', data['id'])])
                if pokemon_existente:
                    # Actualizar si ya existe
                    pokemon_existente.write(vals)
                    _logger.info(f"Pokémon actualizado: {data['name']} (ID: {data['id']})")
                else:
                    # Crear si no existe
                    self.create(vals)
                    _logger.info(f"Pokémon creado: {data['name']} (ID: {data['id']})")
                    
            except requests.exceptions.RequestException as e:
                _logger.error(f"Error de conexión con Pokémon ID {i}: {e}")
            except KeyError as e:
                _logger.error(f"Error en la estructura de datos para Pokémon ID {i}: Campo {e} no encontrado")
            except Exception as e:
                _logger.error(f"Error inesperado con Pokémon ID {i}: {e}")