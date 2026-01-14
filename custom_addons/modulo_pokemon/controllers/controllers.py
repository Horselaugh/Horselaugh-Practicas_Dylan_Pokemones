# -*- coding: utf-8 -*-
# from odoo import http


# class DsPokemon(http.Controller):
#     @http.route('/modulo_pokemon/modulo_pokemon', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulo_pokemon/modulo_pokemon/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulo_pokemon.listing', {
#             'root': '/modulo_pokemon/modulo_pokemon',
#             'objects': http.request.env['modulo_pokemon.modulo_pokemon'].search([]),
#         })

#     @http.route('/modulo_pokemon/modulo_pokemon/objects/<model("modulo_pokemon.modulo_pokemon"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulo_pokemon.object', {
#             'object': obj
#         })

