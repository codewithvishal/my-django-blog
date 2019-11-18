from django.shortcuts import render
from .models import Contact, Entry
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.views.decorators.cache import cache_page

# Create your views here.
@cache_page(60 * 525600)
def index(request):
    data = Entry.objects.filter(status="published")
    print(data[0].post_id)
    return render(request, "blog/index.html", {
        "data": data
    })

@cache_page(60 * 525600)
def post(request, slug_id):
    data = Entry.objects.filter(slug=slug_id)[0]
    print(data)
    return render(request, "blog/post.html", {
        "data": data,
    })

@cache_page(60 * 525600)
def about(request):
    return render(request, "blog/about.html", {})

@cache_page(60 * 525600)
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')
        contact = Contact(name=name, email=email, message=message)
        contact.save()
        
        return HttpResponseRedirect("/contact/")
        
    return render(request, "blog/contact.html")