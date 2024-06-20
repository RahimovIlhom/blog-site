from django.urls import path

from .views import logout_view, login_view, RegisterView

urlpatterns = [
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),
    path('register/', RegisterView.as_view(), name='register'),
]