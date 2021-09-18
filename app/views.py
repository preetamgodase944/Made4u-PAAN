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
    sort='name'
    query=''
    queryName=''
    queryPhone=''
    queryEmail=''
    if searched!='' and searched is not None:
        query=contact_list.filter(message__icontains=searched).order_by(sort)
        queryName=contact_list.filter(name__icontains=searched).order_by(sort)
        queryPhone=contact_list.filter(phonenumber__icontains=searched).order_by(sort)
        queryEmail=contact_list.filter(email__icontains=searched).order_by(sort)
    context={
        'contact_list':contact_list ,
        'query':query,
        'queryName':queryName,
        'queryPhone':queryPhone,
        'queryEmail':queryEmail
    }
    return render(request, 'viewQuery.html',context)

def deleteQuery(request,id):
    deleteQ = Contact.objects.get(phonenumber=id)
    deleteQ.delete() 
    return HttpResponse("Deleted: "+deleteQ.name+" Go Back to view")