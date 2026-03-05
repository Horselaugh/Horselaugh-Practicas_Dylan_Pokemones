from odoo import models, fields, api
import logging

logger = logging.getLogger(__name__)

class Cliente(models.Model):
    _name = 'ecommerce.cliente'
    _description = 'Modelo para registrar los clientes de la tienda'

    #campos relacionados con las compras del cliente
    compras_ids = fields.One2many(
    'ecommerce.compra', 
    'cliente_id', 
    string='Compras')
    
    #campos relacionados con los datos del cliente
    name = fields.Char(string='Nombre', required=True)
    email = fields.Char(string='Correo Electrónico', required=True)
    phone = fields.Char(string='Teléfono')
    address = fields.Text(string='Dirección')

    def ingresar_cliente(self, name, email, phone=None, address=None):
        """ Método para registrar un nuevo cliente en la base de datos """
        cliente = self.env['ecommerce.cliente'].create({
            'name': name,
            'email': email,
            'phone': phone,
            'address': address,
        })
        return cliente