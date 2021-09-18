from django.urls import path,include
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('view/',views.view),
    path('view/delete/<int:id>',views.deleteQuery),
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact')
]