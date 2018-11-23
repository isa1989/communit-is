from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from .models import About, Services
# Create your views here.


def index(request):
    services_list = Services.objects.values()
    context = {'services_list': services_list}
    return render(request, 'polls/index.html',context)



def about(request):
    about_list = About.objects.all()
    context = {'about_list': about_list}
    return render(request, 'polls/about.html', context)

def services(request):
    services_list = Services.objects.values()
    context = {'services_list': services_list}
    return render(request, 'polls/services.html', context)




def contact(request):
    return render(request, 'polls/contact.html')


def footer(request):
    return render(request, 'polls/footer.html')


def partners(request):
    return render(request, 'polls/partners.html')



