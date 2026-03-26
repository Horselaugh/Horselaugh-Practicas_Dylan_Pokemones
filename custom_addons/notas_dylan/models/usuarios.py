from odoo import models, fields
import logging

logger = logging.getLogger(__name__)

class User(models.Model):
    _name = 'notas_dylan.user'
    _description = 'Usuarios'

    #Campos
    name = fields.Char(string = 'Nombres', required=True)
    last_name = fields.Char(string = 'Apellidos', required=True)

    #Campos relacionales
    user_materias = fields.Many2Many(
        'notas_dylan.materias', #Modelo a referenciar
        'materias_user_rel', #Tabla intermediaria
        'notas_dylan.materias',
        string = 'Materias',
    )

    def ingreso_usuario(self, name, last_name):
        user = self.env['notas_dylan.user'].create({
            'Nombre': name,
            'Apellido': last_name,
        })
        return user