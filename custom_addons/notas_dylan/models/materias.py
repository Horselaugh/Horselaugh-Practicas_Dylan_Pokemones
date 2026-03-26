from odoo import models, fields
import logging

logger = logging.getLogger(__name__)

class Materias(models.Model):
    _name = 'notas_dylan.materias'
    _description = 'Materias'

    name = fields.Char(string = 'Nombre de la materia', required=True)
    description = fields.Text(string = 'Descripcion de la materia')
    grades = fields.Integer(string = 'Notas del curso', required=True)
    to_do = fields.Char(string = 'Tarea por hacer', required=True)
    to_do_date = fields.Date(string = 'Fecha de entrega', default=fields.Date.today)
    state = fields.Selection([
        ('asignada', 'Asignada'),
        ('en proceso', 'En proceso'),
        ('hecha', 'Hecha'),
    ], default= 'asignada', string = 'Estado')

    materias_user = fields.Many2Many(
        'notas_dylan.user',
        string = 'Usuario'
    )

    def ingreso_materias(self, name, description=None):
    #Metodo para ingresar de las materias 
        materias = self.env['notas_dylan.materias'].create({
            'name': name,
            'description': description,
        })
        return materias

    def ingreso_notas(self, grades, to_do, to_do_date):
    #Metodo para ingresar las notas
        notas = self.env['notas_dylan.materias'].create({
            'Notas': grades,
            'Tareas': to_do,
            'Fecha de las tareas': to_do_date,
        })
        return notas