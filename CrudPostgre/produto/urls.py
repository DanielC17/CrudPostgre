from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProdutoListView.as_view(), name='produtos'),
    path('<int:pk>', views.ProdutoDetailView.as_view(), name='detalhes'),
    path('add/', views.ProdutoCreateView.as_view(), name='adicionar'),
    path('<int:pk>/edit', views.ProdutoUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete', views.ProdutoDeleteView.as_view(), name='delete')
]

