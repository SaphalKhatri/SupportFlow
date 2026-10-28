from rest_framework import serializer
from .models import Ticket

class UserBriefSerializer(serializers.Serializer):
    id= serializer.IntegerField(read_only=True)
    username= serializer.CharField(read_only=True)
    email= serializer.EmailField(read_only=True)
    role= serializer.CharField(read_only=True)

class TicketListSerializer(serializers.Serializer):
    creator= UserBriefSerializer(read_only=True)
    assigned_agent=UserBriefSerializer(read_only=True)
    class Meta:
         model= Ticket
         fields=['id','ticket_number','title','category','priority','status','creator','assigned_agent','created_at','updated_at','resolved_at',]

class TicketCreateSerializer(serializers.Serializer):
    class Meta:
        model=Ticket
        fields=['id','ticket_number','title','description','category','priority']
        read_only=['id','ticket_number']

    def create(self,validated_data):
        user= self.context['request'].user 
        return Ticket.objects.create(create=user,**validated_data)