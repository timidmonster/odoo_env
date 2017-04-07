# -*- coding: utf-8 -*-
from openerp import http

# class SCall(http.Controller):
#     @http.route('/s_call/s_call/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/s_call/s_call/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('s_call.listing', {
#             'root': '/s_call/s_call',
#             'objects': http.request.env['s_call.s_call'].search([]),
#         })

#     @http.route('/s_call/s_call/objects/<model("s_call.s_call"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('s_call.object', {
#             'object': obj
#         })
class S_call(http.Controller):
    @http.route('/s_call/s_call/', auth='public', website=True)
    def idx(self, **kw):
        Number = http.request.env['s_call.number']
        return http.request.render('s_call.idx',{
            'number' : Number.search([])
        })

        # return "Hello, as usual"
        # return http.request.render('s_call.content')
