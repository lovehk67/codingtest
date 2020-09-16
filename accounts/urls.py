from django.urls import path, include
from . import views
from accounts.api.router import router

urlpatterns = [
    path('rest_api/', include(router.urls)),
    path('', views.index),
]