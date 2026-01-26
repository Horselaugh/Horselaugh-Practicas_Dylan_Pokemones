# -*- coding: utf-8 -*-
{
    'name': "Sistema Pokémon",
    'summary': "Gestión de entrenadores Pokémon y sus capturas",
    'description': """
        Módulo completo para gestionar entrenadores Pokémon, sus Pokémon capturados y el registro de capturas.
        
        Características:
        - Gestión de entrenadores con diferentes categorías
        - Base de datos de Pokémon cargados desde la API oficial
        - Registro de capturas con fecha y estado
        - Conteo automático de Pokémon capturados por entrenador
        - Integración con PokeAPI para cargar información real de Pokémon
    """,
    'author': "Dylan Diaz",
    'website': "https://www.dylandiaz.com",
    'category': 'Tools',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/pokemon_lista.xml',
        'views/pokemon_detalles.xml',
        'views/captura.xml',
        'views/entrenador.xml',
        'views/menu.xml',
    ],
    'demo': [
        'demo/demo.xml',
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