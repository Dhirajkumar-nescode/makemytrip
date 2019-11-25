from django.shortcuts import render
from .models import Destination
# Create your views here.

def index(request):
    dest1 = Destination()
    dest1.name='Mumbai'
    dest1.desc='Place of peace'
    dest1.price=800
    dest1.img='destination_4.jpg'
    dest1.offer=False

    dest2 = Destination()
    dest2.name='Bihar'
    dest2.desc='Genius people'
    dest2.price=700
    dest2.img='destination_5.jpg'
    dest2.offer=True

    dest3 = Destination()
    dest3.name='Delhi'
    dest3.desc='Beautiful city'
    dest3.price=900
    dest3.img='destination_9.jpg'
    dest3.offer=False
   

    dests=[dest1,dest2,dest3]

    return  render(request, "index.html",{'dests':dests})