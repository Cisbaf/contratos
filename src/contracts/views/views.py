from django.shortcuts import render, redirect
from contracts.models import Contract
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.models import CustomUser
import datetime
from dateutil.relativedelta import relativedelta


@login_required(login_url='contract_login')
def index(request):
    if not request.user.is_authenticated:
        return redirect("contract_login")
    contracts = Contract.objects.filter(fiscais=request.user)
    date_now = datetime.date.today()
    for contract in contracts:
        diferenca_meses = relativedelta(contract.end_date, date_now).months + relativedelta(contract.end_date, date_now).years * 12
        if diferenca_meses > 0:
            contract.diference = {'date': diferenca_meses, 'type': 'month'}
        else:
            diferenca_dias = (contract.end_date - date_now).days
            contract.diference = {'date': diferenca_dias, 'type': 'day'}
    context = {
        'contracts': contracts,
        'search_page': True,
    }
    return render(request, 'contract_index.html', context=context)


def contract_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('contract_index')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login_page.html')

def contract_logout(request):
    logout(request)
    return redirect('contract_login')