from odoo import models, fields, api    

class DetallesCompra(models.Model):
    _name = 'ecommerce.detalles_compra'
    _description = 'Detalles de Compra'
    
    # Relación Many2one con compra (DEBE llamarse compra_id para la relación One2many)
    compra_id = fields.Many2one(  
        'ecommerce.compra', 
        string='Compra',
        ondelete='cascade',
        required=True)

    # Relación Many2one con producto
    producto_id = fields.Many2one(
        'ecommerce.producto_api', 
        string='Producto', 
        required=True)

    # Datos de la compra
    cantidad = fields.Integer(
        string='Cantidad', 
        required=True, 
        default=1)
    
    # Campo calculado para el total
    total = fields.Float(
        string='Total', 
        compute='_compute_total', 
        store=True)

    @api.depends('producto_id', 'cantidad')
    def _compute_total(self):
        for detalle in self:
            if detalle.producto_id and detalle.cantidad:
                detalle.total = detalle.producto_id.price * detalle.cantidad
            else:
                detalle.total = 0