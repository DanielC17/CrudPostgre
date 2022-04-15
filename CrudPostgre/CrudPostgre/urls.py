
from django.urls import path, include


urlpatterns = [
    path('produto/', include('produto.urls')),
]
