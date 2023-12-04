from django.http        import HttpResponse
from django.shortcuts   import render
from player.models      import Player
from utils.verb         import Aller



def home(request):
    context = {'title': "Rogue-lite + conjugaison"}

    return render(request, 'home.html', context)



def test(request):
    context = {
        'title': "Testing",
        'players': Player.objects.all()[:2],
    }

    return render(request, 'test.html', context)



def player(request):
    context = {'title': "Player's choice"}

    return render(request, 'player.html', context)



def sentence(request):
    context = {'sentence': Aller.present()}

    return render(request, 'components/sentence.html', context)

