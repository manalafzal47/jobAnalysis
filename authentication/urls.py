from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name="authentication"),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('signout', views.signout, name="signout"),
]