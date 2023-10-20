from django.shortcuts import render

rooms = [
    {'id':1,'name':"Let's learn python"},
    {'id':2,'name':"Design with me"},
    {'id':3,'name':"Developers"},
]

# Create your views here.
def home(request):
    return render(request, 'home.html', {'rooms':rooms})


def room(request):
    return render(request, 'room.html')
