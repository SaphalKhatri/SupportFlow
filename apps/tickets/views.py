from django.shortcuts import render
from rest_framework.response import Response 
from .models import Ticket
from .serializer import(
    TicketListSerializer,TicketDetailSerializer,TicketCreateSerializer
)

# Create your views here.
class TicketView(viewsets.ModelViewset):
    permission_classes=[permissions.IsAuthenticated]

    def get_queryset(self):
        user=self.request.user
        if user.is_staff or user.role in ['agent','admin']:
            return Ticket.objects.select_related('creator','assigned_agent').all()
        return Ticket.objects.select_related('creator','assigned_agent').filter(creator=user)
    
    def get_serializer_class(self):
        if self.action =='create':
            return TicketCreateSerializer
        elif self.action in ['retrieve','update','partial_update']:
            return TicketDetailSerializer
        return TicketListSerializer