from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name = 'home_page'),
    path('update/<str:pk>/',views.update,name = 'update_page'),
    path('delete/<str:pk>/',views.delete,name = 'delete_page'),
]