from django.urls import path
from .views import register, works, insert_sample_data

urlpatterns = [
    path('register', register, name='register'),
    path('works', works, name='works'),
    path('insert_sample_data', insert_sample_data, name='insert_sample_data'),
]
