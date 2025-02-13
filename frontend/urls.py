# frontend/urls.py
from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'), 
    path('upload/', views.upload_image, name='upload_image'),
    # path('login/', csrf_exempt(auth_views.LoginView.as_view()), name='login'),
    # path('images/', views.image_list, name='image_list'),
    path('login/', views.login_view, name='login'), 
    path('upload-form/', views.upload_form, name='upload'), 
]

