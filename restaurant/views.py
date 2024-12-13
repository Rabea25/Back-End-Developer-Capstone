from django.shortcuts import render
from . import serializers
from rest_framework import generics
from .models import Menu, Booking
from rest_framework.permissions import IsAuthenticated, IsAdminUser
# Create your views here.
def index(request):
    return render(request, 'index.html')

class MenuListCreate(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = serializers.MenuSerializer

class SingleMenuItem(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = serializers.MenuSerializer

class BookingListCreate(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = serializers.BookingSerializer

class BookingEdit(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Booking.objects.all()
    serializer_class = serializers.BookingSerializer