# -*- coding: utf-8 -*-
{
    'name': "Grade Teacher",
    'summary': "Gestión de calificaciones de profesores",
    'description': """
        Módulo completo para gestionar calificaciones de profesores, estudiantes y asignaturas.
        
        Características:
        - Gestión de profesores con diferentes categorías
        - Base de datos de estudiantes y asignaturas
        - Registro de calificaciones con fecha y estado
        - Conteo automático de calificaciones por profesor
    """,
    'author': "Dylan Diaz",
    'website': "https://www.dylandiaz.com",
    'category': 'Tools',
    'version': '0.1',
    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',  # Primero permisos
        'views/teacher_lista.xml',       # Vista TREE primero
        'views/teacher_detalles.xml',    # Vista FORM después
        'views/student.xml',             # Vistas de estudiantes
        'views/subject.xml',             # Vistas de asignaturas
        'views/grade.xml',               # Vistas de calificaciones
        'views/menu.xml',                # Menús al final
    ],
    'demo': [
        'data/cargar_api.xml',
    ],

    'images': [
        'static/description/icon.png',
    ],

    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}