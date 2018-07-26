from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    # url(r'^$', views.AddShoes, name="addShoes"),
    path('list/', views.ShoesListView.as_view(), name="shoesList"),
    path('unauthorized/', views.HttpResponseRedirect),
    path('add/', views.AddShoes.as_view(), name="addShoes"),
    url(r'^searchResult/$', views.shoeQuery, name='query'),
]