from django.urls import path
from .views import home, cafe_menu, details, login_view, register_view
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('cafe/', views.cafe_menu, name='cafe'), # Menu page
    path("details/<int:id>/", views.details, name="details"),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
]

