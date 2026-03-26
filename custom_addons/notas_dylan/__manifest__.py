# -*- coding: utf-8 -*-
{
    'name': "Sistema de gestion de notas",
    'summary': "Gestión de Notas",
    'description': """
        Módulo completo para gestionar las notas
    """,
    'author': "Dylan Diaz",
    'website': "https://www.dylandiaz.com",
    'category': 'Tools',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',  # Primero permisos
        'views/materias_views.xml',
        'views/usuarios_views.xml',
        'views/menu.xml',                # Menús al final
    ],

    'images': [
        'static/description/icon.png',
    ],

    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}