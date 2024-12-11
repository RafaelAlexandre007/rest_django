from django.urls import path
from .views import BookListCreateView, BookRetrieverUpdateDestroyView

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-creates'),
    path('books/<int:pk>/', BookRetrieverUpdateDestroyView.as_view(), name='book-detail'),
]
