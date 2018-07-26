from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    # path('admin/', views.UpdateInfo.as_view(), name ='admin'),
    # path('update/', views.UpdateInfo.as_view(), name ='change'),
    url(r'^update/$', views.change, name='change'),
   
]