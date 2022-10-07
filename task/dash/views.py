from django.http import HttpResponse
from .models import Table
from django.shortcuts import render
import json

# Create your views here.

def home(request):
    return render(request,'home.html')

def well_data_view(request):
    well_id=request.GET.get('well')
    posts=Table.objects.filter(api_well_number=well_id).values('oil','gas','brine')
    lists=list(posts)
    data = json.dumps(lists)
    return HttpResponse(data,content_type='application/json')
