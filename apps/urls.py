from django.urls import path
from .views import CSRFView, RegisterView, LoginView, LogoutView, CurrentUserView

urlpatterns = [
    path('csrf/', CSRFView.as_view(), name='auth-csrf'),
    path('register/', RegisterView.as_view(), name='auth-register'),
    path('login/', LoginView.as_view(), name='auth-login'),
    path('logout/', LogoutView.as_view(), name='auth-logout'),
    path('me/', CurrentUserView.as_view(), name='auth-me'),
]