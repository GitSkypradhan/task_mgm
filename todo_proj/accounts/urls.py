from django.urls import path
from . import views
from .views import CustomPasswordResetView

urlpatterns = [

    path("", views.login_user,name='login'),
    path("logout/", views.logout_user,name='logout'),
    path('register/', views.register, name='register'),
    path('password-reset/', CustomPasswordResetView.as_view(), name='password_reset'),

]
