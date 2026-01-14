from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class CapturaPokemon(models.Model):
    _name = 'pokemon.captura'
    _description = 'Captura de Pokémon'
    
    # Campos básicos
    entrenador_id = fields.Many2one(
        'pokemon.entrenador',
        string='Entrenador',
        required=True
    )
    
    pokemon_id = fields.Many2one(
        'pokemon.pokemon',
        string='Pokémon',
        required=True
    )
    
    fecha_captura = fields.Datetime(
        string='Fecha de Captura',
        default=fields.Datetime.now
    )
    
    # Campos relacionados (para fácil visualización)
    pokemon_name = fields.Char(
        string='Nombre Pokémon',
        related='pokemon_id.name',
        readonly=True
    )
    
    entrenador_nombre = fields.Char(
        string='Nombre Entrenador',
        related='entrenador_id.name',
        readonly=True
    )
    
    # Estado simple
    estado = fields.Selection([
        ('capturado', 'Capturado'),
        ('liberado', 'Liberado'),
    ], default='capturado', string='Estado')
    
    @api.model
    def create(self, vals):
        """Al crear captura, añadir Pokémon al entrenador"""
        captura = super(CapturaPokemon, self).create(vals)
        
        # Añadir Pokémon al entrenador
        if captura.entrenador_id and captura.pokemon_id:
            if captura.pokemon_id not in captura.entrenador_id.pokemon_ids:
                captura.entrenador_id.write({
                    'pokemon_ids': [(4, captura.pokemon_id.id)]
                })
                _logger.info(f"{captura.entrenador_id.name} capturó a {captura.pokemon_id.name}")
        
        return captura
    
    def unlink(self):
        """Al eliminar captura, quitar Pokémon del entrenador"""
        for captura in self:
            if captura.entrenador_id and captura.pokemon_id:
                captura.entrenador_id.write({
                    'pokemon_ids': [(3, captura.pokemon_id.id)]
                })
        
        return super(CapturaPokemon, self).unlink()