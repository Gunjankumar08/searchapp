from django.shortcuts import render
from django.http import HttpResponse
from searchapp.models import Product
from searchapp.forms import DataForm
import django_filters


# Create your views here.


def home(request):
    if request.method=="POST":
        datas=request.POST.get('data')
        pro_id=Product.objects.filter(data__icontains=datas)[:20]

        if not pro_id:
            html = '<html><body> <h2>Data Not Found.</h2><br> </body></html>'
            return HttpResponse(html)
        else:
            myData=[]
            for i in pro_id:
                myData.append(i.data)
            html = '<html><body> <h2>Here i have printed Maximum 20 matched data.</h2><br> %s  </body></html>' % myData
            return HttpResponse(html)
    else:
        return render(request, 'home.html')
