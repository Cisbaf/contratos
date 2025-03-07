from django.shortcuts import redirect
from contracts.models import Sector
from django.http.response import JsonResponse
from django.contrib import messages


def get_sectors(request):
    sectores = [sector.to_json() for sector in Sector.objects.all()]
    return JsonResponse(data=sectores, safe=False)


def create_sector(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        if not name:
            messages.error(request, 'Digite o nome do setor')
        else:
            Sector.objects.create(name=name)
        return redirect(request.META.get('HTTP_REFERER', 'contract_dash_sectors'))

    return redirect('contract_dash_sectors')

def rename_sector(request):

    if request.method == 'POST':
        pk = request.POST.get('pk')
        name = request.POST.get('name')
        if not name:
            messages.error(request, 'Digite o nome do setor')
        else:
            sector = Sector.objects.get(pk=pk)
            sector.name = name
            sector.save()
            messages.success(request, f'Setor renomeado!')
        return redirect(request.META.get('HTTP_REFERER', 'contract_dash_sectors'))

    return redirect('contract_dash_sectors')

def delete_sector(request):

    if request.method == 'POST':
        pk = request.POST.get('pk')
        if not pk:
            messages.error(request, 'Algum problema encontrado')
        else:
            sector = Sector.objects.get(pk=pk)
            messages.success(request, f'O setor {sector.name} foi deletado!')
            sector.delete()
        return redirect(request.META.get('HTTP_REFERER', 'contract_dash_sectors'))

    return redirect('contract_dash_sectors')
