from django.urls import path
from . import views

urlpatterns = [
#path("<int:id>", views.index, name='index'),
path('', views.index, name='index'),
path('/', views.index, name='index'),
path('home/', views.index, name='home'),
path('tokhaithongtin/', views.tokhaithongtin, name='tokhaithongtin'),
path('ktrthongtin/', views.ktrthongtin, name='ktrthongtin'),
path('tokhaitren14/', views.tokhaitren14, name='tokhaitren14'),
path('tokhaiduoi14/', views.tokhaiduoi14, name='tokhaiduoi14'),
path('laythongtin/',views.laythongtin, name='laythongtin'),
path('tracuu/', views.tracuu, name='tracuu'),
path('thoigiannhanhochieu/', views.thoigiannhanhochieu, name='thoigiannhanhochieu'),
#path('huongdan', views.huongdan, name='huongdan'),
#path('tracuu', views.tracuu, name='tracuu'),
]