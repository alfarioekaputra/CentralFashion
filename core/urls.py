from django.urls import path

from core import views as core_view


urlpatterns = [
    path('', core_view.home, name='homepage'),
    path('dashboard/', core_view.dashboard, name='dashboard'),
]