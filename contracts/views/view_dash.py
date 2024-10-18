from django.shortcuts import render
from contracts.models import  Sector, Contract
from accounts.models import CustomUser
import json

def index(request):
    print('hola')
    return render(request, 'contract_dash_index.html')

def dash_fiscais(request, pk: int=None):
    context = {
        'data_users': CustomUser.get_users(),
        'search_page': True,
        'term': pk if pk else None
        }
    return render(request, 'contract_dash_fiscais.html', context=context)

def dash_sectors(request):
    sectors = Sector.objects.all()
    for sector in sectors:
        sector.users = CustomUser.get_users(sector=sector)
    context = {'sectors': sectors}
    return render(request, 'contract_dash_sectors.html', context=context)

def dash_contract(request):

    contracts = Contract.objects.all()
    for contract in contracts:
        contract.att_json()
    context = {
        'contracts': contracts,
        'search_page': True,
        'tas': json.dumps(Contract._meta.get_field('ta').choices)
    }
    return render(request, 'contract_dash_contract.html', context=context)