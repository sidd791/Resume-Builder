from django.urls import path, include
from . import views

app_name = 'resumeApp'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:id>', views.resume, name = 'resume')
]
