from django.urls import path
from . import views

urlpatterns = [
#path("<int:id>", views.index, name='index'),
path('', views.index, name='index'),
path('tokhaithongtin/', views.tokhaithongtin, name='tokhaithongtin'),
path('ktrathongtin/', views.ktrathongtin, name='ktrathongtin'),
path('tokhaitren14/', views.tokhaitren14, name='tokhaitren14'),
path('tokhaiduoi14', views.tokhaiduoi14, name='tokhaiduoi14'),

#path('huongdan', views.huongdan, name='huongdan'),
#path('tracuu', views.tracuu, name='tracuu'),
]