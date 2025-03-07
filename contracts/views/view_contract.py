
from django.shortcuts import redirect
from contracts.models import Contract
from django.contrib import messages
from datetime import datetime
from faker import Faker
from accounts.models import CustomUser
import random, re
from django.contrib.auth.decorators import login_required

fake = Faker()


def create_contracts_fakes(request):
    fiscais = CustomUser.objects.all()
    for _ in range(20):
        contract = Contract.objects.create(
            object = fake.passport_number(),
            contract = fake.credit_card_number(),
            company = fake.company(),
            start_date = fake.date(),
            end_date = fake.date()
        )
        for _ in range(2):
            contract.fiscais.add(random.choice(fiscais))
        contract.save()


def sanitize_text_for_json(text: str) -> str:
    text = text.replace('"', "'")
    text = text.replace('(', " ")
    text = text.replace(')', " ")
    text = text.replace(':', " ")
    return text

@login_required(login_url='contract_login')
def contract_request_options(request):
    if request.method == 'POST':
        method = request.POST.get('_method')
        if not method:
            raise
        form = request.POST
        object_contract = sanitize_text_for_json(form.get('object_contract'))
        number_contract = form.get('number_contract')
        number_process = form.get('number_process')
        cnpj_cpf = form.get('cnpj_cpf')
        value_global = form.get('value_global')
        value_mensal = form.get('value_mensal')
        company = form.get('company')
        fiscais = form.getlist('fiscais')
        start_date = form.get('start_date')
        end_date = form.get('end_date')
        font = form.get('font')
        ta = form.get('ta')
        list_fiscais = [CustomUser.get_user(pk=pk) for pk in fiscais]
        match method:
            case 'POST':
                contract = Contract.objects.create(
                    object=object_contract,
                    number_contract=number_contract,
                    number_process=number_process,
                    company=company,
                    cnpj_cpf=cnpj_cpf,
                    value_global=value_global,
                    value_mensal=value_mensal,
                    start_date = datetime.strptime(start_date, '%d/%m/%Y').date(),
                    end_date = datetime.strptime(end_date, '%d/%m/%Y').date(),
                    font=font,
                    ta=ta
                )
                contract.fiscais.set(list_fiscais)
                messages.success(request, f'Contrato {number_contract} criado!')
            case 'PUT':
                pk = form.get('pk')
                contract = Contract.objects.get(pk=pk)
                contract.object = object_contract
                contract.number_contract = number_contract
                contract.number_process = number_process
                contract.company = company
                contract.cnpj_cpf = cnpj_cpf
                contract.value_global = value_global
                contract.value_mensal = value_mensal
                contract.fiscais.clear()
                contract.fiscais.set(list_fiscais)
                contract.start_date = datetime.strptime(start_date, '%d/%m/%Y').date()
                contract.end_date = datetime.strptime(end_date, '%d/%m/%Y').date()
                contract.font = font
                contract.ta = ta
                contract.save()
                messages.success(request, f'Contrato {number_contract} atualizado!')
    return redirect(request.META.get('HTTP_REFERER', 'contract_dash_contract'))

@login_required(login_url='contract_login')
def contract_delete(request, pk):
    if not request.user.is_staff:
        messages.success(request, f'Apenas o administrador pode deletar!')
    else:
        contract = Contract.objects.get(pk=pk)
        contract.delete()
        messages.success(request, f'Contrato {contract.number_contract} deletado!')
    return redirect(request.META.get('HTTP_REFERER', 'contract_dash_contract'))
