from django.urls import path, re_path
from board import views


urlpatterns = [
    path('', views.index, name="index"),
    path('select/', views.select, name="select"),
    path('select/<int:value>', views.select, name="select"),
    #re_path(r'^select/(?P<value>[0-9]{4}/$', views.select, name="re_select"),
    path('result/', views.result, name="result"),
]
