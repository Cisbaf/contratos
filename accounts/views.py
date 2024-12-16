from django.shortcuts import redirect
from .models import CustomUser
from contracts.models import Sector
from django.contrib import messages
from django.http.response import JsonResponse
from django.contrib import messages
import random


def get_users(request):
    context = [user.infos_json for user in CustomUser.get_users()]
    return JsonResponse(data=context, safe=False)

def create_user(request):
    if request.method == 'POST':
        method = request.POST.get('_method')
        if not method:
            raise
        form = request.POST
        name = form.get('name')
        email = form.get('email')
        cell = form.get('cell')
        sector = form.get('sector')
        parts = str(name).split(' ')
        first_name = parts[0]
        last_name = " ".join(parts[1:]) if len(parts) > 1 else ""
        match method:
            case 'POST':
                password = form.get('password')
                
                user = CustomUser.objects.create(
                    username=email,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    cell_phone=cell,
                    sector=Sector.objects.get(pk=sector),

                )
                user.set_password(password)
                user.save()
                messages.success(request, f'Fiscal {first_name} {last_name} !')
            case 'PUT':
                pk = form.get('pk')
                user = CustomUser.objects.get(pk=pk)
                user.first_name = first_name
                user.last_name = last_name
                user.email = email
                user.cell_phone = cell
                user.sector = Sector.objects.get(pk=sector)
                user.save()
                messages.success(request, f'Fiscal {first_name} {last_name} atualizado!')

    return redirect(request.META.get('HTTP_REFERER', 'contract_dash_fiscais'))

def delete_user(request, pk):
    if not request.user.is_staff:
        messages.success(request, f'Apenas o administrador pode deletar!')
    else:
        user = CustomUser.objects.get(pk=pk)
        user.delete()
        messages.success(request, f'Fiscal {user.get_full_name()} deletado!')
    return redirect(request.META.get('HTTP_REFERER', 'contract_dash_fiscais'))



from faker import Faker

def register_fiscais_fake(request):
    # fake = Faker()
    # for _ in range(40):
    #     email = fake.email()
    #     user = CustomUser.objects.create(
    #     username=email,
    #     password=fake.password(),
    #     first_name=fake.first_name(),
    #     last_name=fake.last_name(),
    #     app=App.objects.get(name="contract"),
    #     email=email)
    #     DataUser.objects.create(
    #         user=user,
    #         cell_phone='9999999',
    #         sector=random.choice(Sector.objects.all())
    #     )
    pass

def define_color(request, index: int):
    if not request.user.pk:
        return redirect('/login')
    user = CustomUser.get_user(request.user.pk)
    match index:
        case 0:
            messages.success(request, "Tema amarelo atualizado!")
            user.theme = """
            :root {
            --primary-color: #ffd800;

            --icon-bc: #ffd800;
            --icon-bc-hover: #ffc400;
            --icon-c: black;

            --menu-bc: #ffff;
            --menu-bc-hover: #f0f0f0;
            --menu-c: rgb(22, 22, 22);
            }
            """
            user.save()
        case 1:
            messages.success(request, "Tema branco atualizado!")
            user.theme = """
            :root {
            --primary-color: #f6f7f9;

            --icon-bc: #626262;
            --icon-bc-hover: #333333;
            --icon-c: white;

            --menu-bc: #626262;
            --menu-bc-hover: #333333;
            --menu-c: white;
            }
            """
            user.save()
        case 2:
            messages.success(request, "Tema azul atualizado!")
            user.theme = """
            :root {
                --primary-color: #247BA0;

                --icon-bc: #247BA0;
                --icon-bc-hover: #1b5974;
                --icon-c: rgb(236, 236, 236);

                --menu-bc: #ffff;
                --menu-bc-hover: #f0f0f0;
                --menu-c: rgb(22, 22, 22);
                }
            """
            user.save()


    return redirect(request.META.get('HTTP_REFERER', 'contract_dash'))
