from django.urls import path
from . import views
from django.conf.urls import url
from shoes import views as shoesView

urlpatterns = [
    url(r'^test/$', views.tranHistory, name='addHistory'),
    path('list/', views.TranListView.as_view(), name="tranList"),
    url(r'^transaction_detail/$', views.tranDetails, name='detailHistory'),

]