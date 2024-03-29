from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http import HttpResponseRedirect, HttpResponse
from django.template.loader import render_to_string
from mainbase.models import Progress, Province
from datetime import datetime, timedelta
from django.utils import timezone
from django.conf import settings
import json

def index(request):
    starter   = timezone.now() - timedelta(days=30)
    data = []
    for single_date in (starter + timedelta(n) for n in range(31)):
        progres = Progress.objects.filter(tanggal=single_date.strftime('%Y-%m-%d'))
        if progres.count() > 0:
            progres = progres.latest('id')
            rcd = {}
            rcd['date'] = progres.tanggal
            for k,v in json.loads(progres.data).items():
                rcd[k] = v            
            data.append(rcd)

    prog = Progress.objects.all()
    if prog.count() > 0:
        tme = prog.latest('id').created_at
    else:
        tme = datetime.now()    
    return JsonResponse({
            'last_updated': tme.isoformat(),
            'monitoring': data
        })
    



    

    
        


