from rest_framework import permissions

class IsTicketParticipantsOrStaff(permissions.BasePermission):
    def has_object_permissions(self,request,view,obj):
        if request.user.is_staff or request.user.role in ['agent','admin']:
            return True 
        return obj.creator==request.user
        