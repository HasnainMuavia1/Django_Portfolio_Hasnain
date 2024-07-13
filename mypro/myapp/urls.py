"""
URL configuration for mypro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
urlpatterns = [
    path('', views.home, name='home'),
    path('Login/', views.Login, name='login'),
    path('skills/', views.skills, name='skills'),
    path('signup/',views.signup,name='signup'),
    path('Dashboard/',views.dashboard,name='Dashboard'),
    path('logout/',views.mylogout,name='logout'),
    path('activate/<str:id>/', views.activateAccount, name='activate'),
    path('rest_view/',PasswordResetView.as_view(template_name='password_reset.html'), name='reset_view'),
    path('rest_done/done/', PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password_confirm/<uidb64>/<token>',PasswordResetConfirmView.as_view(template_name="password_confirm.html"), name='password_reset_confirm'),
    path('password_reset_complete/',PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    path('hireMe/',views.hireMe, name='hire'),
    path('data/<str:name>/',views.data,name='data'),
    path('delete/<str:id>/<str:name>/',views.delete,name='delete'),
    path('edit/<str:id>/<str:name>/',views.edit,name='edit'),

]
