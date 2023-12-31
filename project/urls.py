from django.contrib import admin
from django.urls    import path
from .              import views

urlpatterns = [
    path('',            views.home,         name='home'),
    path('player',      views.player,       name='player'),
    path('test',        views.test,         name='test'),
    path('sentence',    views.sentence,     name='sentence'),

    path('admin/',  admin.site.urls,    name='admin'),
]
