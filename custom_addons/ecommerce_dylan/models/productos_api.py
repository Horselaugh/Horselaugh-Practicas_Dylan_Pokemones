from odoo import models, fields, api
import requests
import logging

_logger = logging.getLogger(__name__)

class ProductosAPI(models.Model):
    _name = 'ecommerce_dylan.productos_api'
    _description = 'Productos API'

    name = fields.Char(string='Nombre del Producto', required=True)
    price = fields.Float(string='Precio', required=True)
    description = fields.Text(string='Descripción')
    category = fields.Char(string='Categoría')
    image = fields.Char(string='URL de la Imagen')

    @api.model
    def cargar_api_productos(self):
        url = "https://fakestoreapi.com/products"
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                data = response.json()
                for product in data:
                    vals = {
                        'name': product['title'],
                        'price': product['price'],
                        'description': product['description'],
                        'category': product['category'],
                        'image': product['image'],
                    }
                    self.create(vals)
            else:
                _logger.warning("Error al obtener productos de la API")
        except Exception as e:
            _logger.error(f"Error al cargar productos desde la API: {e}")


    @api.model
    def cargar_api_detalles(self):
        for i in range(1, 19):
            url = f"https://fakestoreapi.com/products/{i}"
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                data = response.json()
                vals = {
                    'name': data['title'],
                    'price': data['price'],
                    'description': data['description'],
                    'category': data['category'],
                    'image': data['image'],
                }
                self.create(vals)
            else:
                _logger.warning(f"Producto {i} no disponible o error de API")
        except Exception as e:
            _logger.error(f"Error al cargar producto {i} desde la API: {e}")