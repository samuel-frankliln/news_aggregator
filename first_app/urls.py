from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('international',views.international,name='international'),
    path('who',views.who,name="who"),
    path('bbc',views.bbc,name="bbc"),
    path('toi',views.toi,name="toi"),
    path('ht',views.ht,name="ht"),
    path('national',views.national,name='national'),
]
