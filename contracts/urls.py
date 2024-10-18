from django.urls import path
from .views import view_dash, view_sector, view_contract, views


urlpatterns = [
    # index
    path('', views.index, name="contract_index"),
    path('login', views.contract_login, name="contract_login"),
    path('logout', views.contract_logout, name="contract_logout"),
    # dash
    path('dash/', view_dash.index, name="contract_dash"),
    path('dash/fiscais', view_dash.dash_fiscais, name="contract_dash_fiscais"),
    path('dash/fiscais/<int:pk>', view_dash.dash_fiscais, name="contract_dash_fiscais_pk"),
    path('dash/sectors', view_dash.dash_sectors, name="contract_dash_sectors"),
    path('dash/contracts', view_dash.dash_contract, name="contract_dash_contract"),
    #api contract
    path('contract/options', view_contract.contract_request_options, name="contract_options"),
    path('contract/delete/<int:pk>', view_contract.contract_delete, name="contract_delete"),
    path('contract/fake', view_contract.create_contracts_fakes),
    # api sector
    path('sector/all', view_sector.get_sectors, name="contract_get_sectors"),
    path('sector/create', view_sector.create_sector, name="contract_create_sector"),
]
