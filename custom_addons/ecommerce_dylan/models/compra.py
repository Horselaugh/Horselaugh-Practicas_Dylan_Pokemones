from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class Compra(models.Model):
    _name = 'ecommerce.compra'
    _description = 'Modelo para registrar las compras realizadas por los clientes'

    cliente_id = fields.Many2one(
    'ecommerce.cliente', 
    string='Cliente', 
    required=True)

    producto_id = fields.Many2one(
    'ecommerce.producto_api', 
    string='Producto', 
    required=True)

    cantidad = fields.Integer(string='Cantidad', required=True, default=1)
    total = fields.Float(string='Total', compute='_compute_total', store=True)

    def comprar_producto(self, producto_id, cantidad):
        """ Método para registrar una compra de un producto por parte del cliente """
        compra = self.env['ecommerce.compra'].create({
            'cliente_id': self.id,
            'producto_id': producto_id,
            'cantidad': cantidad,
        })
        return compra

