from django.shortcuts import render, get_object_or_404
#from django.http import HttpResponse
#from django.http import Http404
from .models import Pet

# Create your views here.

def index(request):
    template = "index.html"
    pets = Pet.objects.all() #extracting all pets
    context = {'pets':pets}
    return render(request, template, context)
    #return render(request, "index.html")
    #return HttpResponse("<h1>This is the Adoptions Home Page</h1>")

def pet_detail(request, pet_id):
    template = "pet_details.html"
    pet = Pet.objects.get(id = pet_id) #extracting particular pet
    context = {'pet': pet}
    return render(request, template, context)
    #return HttpResponse("<h2>This is the Pet Detail for Pet number {}</h2>".format(pet_id))
    #return render(request,"pet_details.html", {"pet_number": pet_id})
