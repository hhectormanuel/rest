from django.urls import path
from .api import UserAPIView, get, usuario_detail


app_name='restapp'

urlpatterns = [
    path('', UserAPIView.as_view(), name='usuario_api'),
    path('get/', get, name='get'),
    path('detail/<int:pk>', usuario_detail, name='detail'),
]