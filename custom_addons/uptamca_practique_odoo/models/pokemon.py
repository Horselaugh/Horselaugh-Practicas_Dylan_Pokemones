import requests
from odoo import models, fields, api, _
from odoo.exceptions import UserError

class Pokemon(models.Model):
    _name = 'pokemon'
    _description = 'Pokémon'

    name = fields.Char(string='Nombre', required=True, tracking=True)
    category_id = fields.Many2one('pokemon.category', string='Categoría', tracking=True)
    state = fields.Selection([
        ('loose', 'Libre'),
        ('captured', 'Capturado')
    ], string='Estado', default='loose', tracking=True)
    
    def load_pokemon(self): 
        """Método optimizado para cargar Pokémon."""
        url_base = 'https://pokeapi.co/api/v2/pokemon?limit=151'
        try:
            session = requests.Session()
            response = session.get(url_base, timeout=10)
            response.raise_for_status()
            data = response.json()

            vals_list = []
            for item in data['results']:
                pokemon_name = item['name'].capitalize()

                if self.search_count([('name', '=', pokemon_name)]):
                    continue

                detail_resp = session.get(item['url'], timeout=10)
                detail_data = detail_resp.json()

                # Categoría
                type_name = detail_data['types'][0]['type']['name'].capitalize()
                category = self.env['pokemon.category'].search([('name', '=', type_name)], limit=1)
                if not category:
                    category = self.env['pokemon.category'].create({'name': type_name, 'type': 'pokemon'})

        except requests.exceptions.RequestException as e:
            raise UserError(_("Error de conexión con la API: %s") % e)