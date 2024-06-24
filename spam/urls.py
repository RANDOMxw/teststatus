from django.urls import path
from .views import SpamView, SearchView

urlpatterns = [
    path('mark-spam/', SpamView.as_view()),
    path('search/', SearchView.as_view()),
]
