from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class Compra(models.Model):
    _name = 'ecommerce.compra'
    _description = 'Modelo para registrar las compras realizadas por los clientes'

    # Relación Many2one con el modelo de cliente
    cliente_id = fields.Many2one(
        'ecommerce.cliente', 
        string='Cliente', 
        required=True)

    # Relación One2many con detalles de compra
    detalles_ids = fields.One2many(
        'ecommerce.detalles_compra',
        'compra_id',  # Ahora sí existe en detalles_compra
        string='Detalles de Compra')

    # Campo calculado para el total de la compra
    total_compra = fields.Float(
        string='Total Compra',
        compute='_compute_total_compra',
        store=True)

    @api.depends('detalles_ids.total')
    def _compute_total_compra(self):
        for compra in self:
            compra.total_compra = sum(compra.detalles_ids.mapped('total'))

    def comprar_producto(self, cliente_id, productos):
        """ Método para registrar una compra con múltiples productos """
        # Crear la compra
        compra = self.create({
            'cliente_id': cliente_id,
        })
        
        # Crear los detalles de compra
        DetallesCompra = self.env['ecommerce.detalles_compra']
        for item in productos:
            producto = self.env['ecommerce.producto_api'].browse(item['producto_id'])
            DetallesCompra.create({
                'compra_id': compra.id,
                'producto_id': item['producto_id'],
                'cantidad': item['cantidad'],
            })
        
        return compra