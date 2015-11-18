"""
    Routes Configuration File

    Put Routing rules here
"""
from system.core.router import routes

routes['default_controller'] = 'Welcome'
routes['POST']['/create_note'] = 'Welcome#create'
routes['POST']['/update/<id>'] = 'Welcome#update'
routes['POST']['/delete/<id>'] = 'Welcome#delete'
routes['POST']['/show/<id>'] = 'Welcome#show'
routes['GET']['/index_notes'] = 'Welcome#index_notes'
