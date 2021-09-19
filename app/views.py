from django.shortcuts import render
from .models import Contact
from django.http import HttpResponse
# Create your views here.
def index(request):
    if request.method=="POST":
        contact=Contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        phonenumber=request.POST.get('phonenumber')
        message=request.POST.get('message')
        contact.name=name
        contact.email=email
        contact.phonenumber=phonenumber
        contact.message=message
        contact.save()
        #return HttpResponse("<h1>Thanks for Contacting us</h1>")

    return render(request, 'index.html')

def services(request):
    return render(request, 'services.html')


def contact(request):
    if request.method=="POST":
        contact=Contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        phonenumber=request.POST.get('phonenumber')
        message=request.POST.get('message')
        contact.name=name
        contact.email=email
        contact.phonenumber=phonenumber
        contact.message=message
        contact.save()

    return render(request, 'contact.html')

def view(request):
    contact_list = Contact.objects.all()
    searched=request.GET.get('search')
    sort=''
    sortbpn=''
    sortbn=''
    sortbm=''
    sortbem=''
    sort=request.GET.get('sort')
    que=''
    query=''
    queryName=''
    queryPhone=''
    queryEmail=''
    if searched!='' and searched is not None:
        query=contact_list.filter(message__icontains=searched)
        queryName=contact_list.filter(name__icontains=searched)
        queryPhone=contact_list.filter(phonenumber__icontains=searched)
        queryEmail=contact_list.filter(email__icontains=searched)
        

    if sort !='' and sort is not None:
        if sort=='name':
            sortbn=contact_list.order_by('name')
        elif sort=='message':
            sortbm=contact_list.order_by('message')
        elif sort=='phoneNumber':
            sortbpn=contact_list.order_by('phoneNumber')
        else:
            sortbem=contact_list.order_by('email')

    
    context={
        'contact_list':contact_list ,
        'query':query,
        'queryName':queryName,
        'queryPhone':queryPhone,
        'queryEmail':queryEmail,
        'sort':sort,
        'sortbn':sortbn,
        'sortbpn':sortbpn,
        'sortbem':sortbem
    }
    return render(request, 'viewQuery.html',context)

def deleteQuery(request,id):
    deleteQ = Contact.objects.get(phonenumber=id)
    deleteQ.delete() 
    return HttpResponse("Deleted: "+deleteQ.name+" Go Back to view")