from django.contrib import admin
from django.urls import path ,include
from home import views

urlpatterns = [
    path('', views.logi, name="logi"),
    path('create', views.create, name="create"),
     path('/index', views.index, name="index"),
     path('index', views.index, name="index"),
     path('cart', views.cart, name="cart"),
    path('about', views.about, name="about"),
    path('thanks', views.thanks, name="thanks"),
    path('thanks1', views.thanks1, name="thanks1"),
    path('thanks2', views.thanks2, name="thanks2"),
    path('profile', views.pro, name="pro"),
    path('login', views.logi, name="logi"),
    path('cartin', views.cartin, name="cartin"),
      path('login', views.logi, name="logi"),
    path('display', views.display, name="display"),
    path('logout', views.logou, name="logou"),
    path('remove', views.remove, name="remove"),
    
    #  path('addp', views.addp, name="addp"),
    #  path('thanks', views.thanks, name="thanks"),
    # path('logout', views.logou, name="logou"),

]
