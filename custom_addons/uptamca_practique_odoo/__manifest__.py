# -*- coding: utf-8 -*-
{
    'name': "Uptamca PokéApp",

    'summary': "Gestión de Pokémon integrando PokéAPI",

    'description': """
Módulo para la práctica de Odoo 18 que permite:
- Importar Pokémon desde PokéAPI.
- Gestionar categorías y estados de captura.
- Visualizar imágenes de Pokémon.
    """,

    'author': "Tu Nombre / My Company",
    'website': "https://www.yourcompany.com",

    'category': 'Inventory/Pokédex',
    'version': '1.0',

    # DEPENDENCIAS - Necesitas mail para tracking
    'depends': ['base', 'mail'],

    # DATA - Carga en el orden correcto
    'data': [
        # 1. PRIMERO: Seguridad (los CSV simples funcionan mejor)
        'security/ir.model.access.csv',
        'views/pokemon.xml',
        'views/menu.xml',
    ],
    
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}