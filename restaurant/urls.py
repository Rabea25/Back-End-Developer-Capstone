from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuListCreate.as_view(), name='menu'),
    path('menu/<int:pk>/', views.SingleMenuItem.as_view(), name='single_menu_item'),
    path('booking/', views.BookingListCreate.as_view(), name='booking'),
    path('booking/<int:pk>/', views.BookingEdit.as_view(), name='booking_edit'),
] 
