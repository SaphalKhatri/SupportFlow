from rest_framework.routers import DefaultRouter
from .views import TicketView

router = DefaultRouter()
router.register(r'tickets',TicketView,basename='ticket')
urlpatterns= router.urls