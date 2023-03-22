from django.urls import path
from . import views


app_name='web'


urlpatterns = [
    path('', views.contact_list, name='contact_list'),
    path('contact_detail/<int:pk>/', views.contact_detail, name='contact_detail'),
    path('new/', views.contact_create, name='contact_create'),
    path('edit/<int:pk>/', views.contact_update, name='contact_update'),
    path('delete/<int:pk>/', views.contact_delete, name='contact_delete'),
]
