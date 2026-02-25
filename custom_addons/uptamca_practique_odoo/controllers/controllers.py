# -*- coding: utf-8 -*-
# from odoo import http


# class UptamcaPractiqueOdoo(http.Controller):
#     @http.route('/uptamca_practique_odoo/uptamca_practique_odoo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/uptamca_practique_odoo/uptamca_practique_odoo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('uptamca_practique_odoo.listing', {
#             'root': '/uptamca_practique_odoo/uptamca_practique_odoo',
#             'objects': http.request.env['uptamca_practique_odoo.uptamca_practique_odoo'].search([]),
#         })

#     @http.route('/uptamca_practique_odoo/uptamca_practique_odoo/objects/<model("uptamca_practique_odoo.uptamca_practique_odoo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('uptamca_practique_odoo.object', {
#             'object': obj
#         })

