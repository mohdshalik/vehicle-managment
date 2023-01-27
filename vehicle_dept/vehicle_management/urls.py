from django.urls import path
from .views import vehicle,login,logout,vehicle_register,vehicle_update,vehicle_delete

from . import views

urlpatterns=[
    path('',vehicle.as_view(),name='index'),
    path('login',login.as_view(),name="login"),
    path('logout',logout.as_view(),name='logout'),
    path('vehicle',vehicle_register.as_view(),name='vehicle_register'),
    path('update/<int:pk>',vehicle_update.as_view(),name='vehicle_update'),
    path('<int:pk>/delete/', vehicle_delete.as_view(), name='vehicle_delete')

]