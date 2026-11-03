from django.shortcuts import render
from rest_framework.response import Response 
from .models import Ticket
from .serializer import(
    TicketListSerializer,TicketDetailSerializer,TicketCreateSerializer
)
from .permissions import IsTicketParticipantsOrStaff

# Create your views here.
class TicketView(viewsets.ModelViewset):
    permission_classes=[permissions.IsAuthenticated,IsTicketParticipantsOrStaff]

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

    def perform_update(self,serializer):
        user= self.request.user
        if user.role=='customer' and not user.is_staff:
            if 'status' in serializer.validated_data or 'assigned_agent' in serializer.validated_data:
                raise serializer.ValidationError("customer vannot change ticket status or assignemnt")\
        serializer.save()