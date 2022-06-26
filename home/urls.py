from django.contrib import admin
from django.urls import path ,include
from home import views

urlpatterns = [
    path('', views.index, name="index"),
    path('create', views.create, name="create"),
    path('about', views.about, name="about"),
    path('thanks', views.thanks, name="thanks"),
    path('thanks1', views.thanks1, name="thanks1"),
    path('thanks2', views.thanks2, name="thanks2"),
    path('login', views.logi, name="logi"),
    path('logout', views.logou, name="logou"),
    #  path('thanks', views.thanks, name="thanks"),
    # path('logout', views.logou, name="logou"),

]
