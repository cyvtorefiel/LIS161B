from django.urls import path
from . import views

urlpatterns = [
    #http://127.0.0.1:8000/adoptions/
    path('', views.index, name = "index"),
    #http://127.0.0.1:8000/adoptions/99
    #http://127.0.0.1:8000/adoptions/2
    path('<int:pet_id>', views.pet_detail, name = "pet_detail" ),

]
