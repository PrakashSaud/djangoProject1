from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('account/', include("django.contrib.auth.urls")),
    path('signup/', views.SignUp.as_view(), name='signup'),
    
]