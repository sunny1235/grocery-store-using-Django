from django.urls import path
from . import views

urlpatterns = [
      
       path('', views.index, name = "home"),
       path('shop', views.shop, name = "shop"),
       path('blog', views.blog, name = "blog"),
       path('contact',views.contact, name="contact"),
       path('details/<int:myid>',views.details, name="details"),
       path('reg',views.reg, name="reg"),
       path('login',views.login, name="login"),
]

