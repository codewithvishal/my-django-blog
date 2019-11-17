from django.shortcuts import render
from .models import Contact, Entry
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse

# Create your views here.
def index(request):
    data = Entry.objects.filter(status="published")
    print(data[0].post_id)
    return render(request, "blog/index.html", {
        "data": data
    })

def post(request, slug_id):
    data = Entry.objects.filter(slug=slug_id)[0]
    print(data)
    return render(request, "blog/post.html", {
        "data": data
    })

def about(request):
    return render(request, "blog/about.html", {})

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')
        contact = Contact(name=name, email=email, message=message)
        contact.save()
        
        return HttpResponseRedirect("/blog/contact/")
        
    return render(request, "blog/contact.html")


    