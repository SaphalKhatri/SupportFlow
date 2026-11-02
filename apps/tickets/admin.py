from django.contrib import admin
from .models import Ticket


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('ticket_number', 'title', 'category', 'priority', 'status', 'creator', 'assigned_agent', 'created_at')
    list_filter = ('status', 'priority', 'category', 'created_at')
    search_fields = ('ticket_number', 'title', 'description', 'creator__username', 'creator__email')
    readonly_fields = ('ticket_number', 'created_at', 'updated_at', 'resolved_at')
    autocomplete_fields = ('creator', 'assigned_agent')