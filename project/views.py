from django.http        import HttpResponse
from django.shortcuts   import render



def home(request):
    return render(request, 'home.html')



def player(request):
    context = {'title': "Player's choice"}

    return render(request, 'player.html', context)
