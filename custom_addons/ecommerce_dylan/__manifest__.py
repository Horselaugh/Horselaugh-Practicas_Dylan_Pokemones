# -*- coding: utf-8 -*-
{
    'name': "ecommerce",
    'summary': "Ecommerce_Dylan",
    'description': """
    Modulo para un ecommerce de ejemplo, 
    con funcionalidades básicas para gestionar productos, 
    clientes y pedidos.
    """,
    'author': "Dylan Diaz",
    'website': "https://www.dylandiaz.com",
    'category': 'Tools',
    'version': '0.1',
    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',  # Primero permisos
        'views/list.xml',
        'views/menu.xml',                # Menús al final
    ],
    'demo': [
        'data/cargar_api.xml',
        'demo/demo.xml',
    ],

    'images': [
        'static/description/icon.png',
    ],

    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}