from django.urls import path
from . import views

app_name = "add_quotes"

urlpatterns = [
    path('', views.index, name='home'),
    path('add_author/', views.add_author, name='add_author'),
    path('upend_quote/', views.add_quote, name='upend_quote'),
    path('author/<int:pk>/', views.author_detail, name='author_detail')
]
