from django.db import models
from django.conf import settings
from django.utils import timezone 

# Create your models here.
class Ticket(models.Model):
    TICKET_CHOICES=[
        ('general','General'),
        ('technical','Technical'),
        ('billing','Billing'),
        ('account','Account')
    ]
    PRIORITY_CHOICES=[
        ('low','Low'),
        ('medium','Medium'),
        ('high','High'),
        ('urgent','Urgent')
    ]
    STATUS_CHOICES=[
        ('open','Open'),
        ('in_progress','In Progress'),
        ('resolved','Resolved'),
        ('closed','Closed')
    ]
    ticket_number= models.CharField(max_length=20,unique=True,editable=False,db_index=True)
    title=models.CharField(max_length=20)
    description= models.TextField()
    category= models.CharField(max_length=20,choices=TICKET_CHOICES,default='general')
    priority= models.CharField(max_length=20,,choices=PRIORITY_CHOICES,default='medium')
    status= models.CharField(max_length=20,choices=STATUS_CHOICES,default='open')
    creator= models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True,blank=True,related_name='created-tickets')
    assigned_agent = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='assigned_tickets'
    )
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    resolved_at= models.DateTimeField(null=True,blank=True)

    class Meta:
        ordering=["-created_at"]

    def __str__(self):
        return f"{self.ticket_number or 'New ticket'}-{self.title}"