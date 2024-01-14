from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, generics
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, MenuItemSerializer, BookingSerializer
from .models import Menu, Booking

def sampleView(request):
    return render(request, 'index.html', {}) 

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer
    
class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
    
    
