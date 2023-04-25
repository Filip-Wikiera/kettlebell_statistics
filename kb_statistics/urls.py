from django.urls import path
from . import views

urlpatterns = [
    path('kb_statistics/', views.kb_statistics, name='kb_statistics'),
]
