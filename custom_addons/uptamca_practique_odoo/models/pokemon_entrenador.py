from odoo import models, fields, api

class entrenador(models.Model):
    _name = 'pokemon.entrenador'
    _description = 'entrenador Pokemon'
    #_inherits = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Nombre", required=True, tracking=True)
    category = fields.Selection([
        ('novice', 'Novato'),
        ('advanced', 'Avanzado'),
        ('master', 'Maestro')
    ], string="Categoría", default='novice', tracking=True)
  

