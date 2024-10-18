from django.shortcuts import redirect
from contracts.models import Sector
from django.http.response import JsonResponse


def get_sectors(request):
    sectores = [sector.to_json() for sector in Sector.objects.all()]
    return JsonResponse(data=sectores, safe=False)


def create_sector(request):

    if request.method == 'POST':
        method = request.POST.get('_method')
        name = request.POST.get('name')
        Sector.objects.create(name=name)
        return redirect(request.META.get('HTTP_REFERER', 'contract_dash_sectors'))

    return redirect('contract_dash_sectors')
