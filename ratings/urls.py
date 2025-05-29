from django.urls import path
from . import views

urlpatterns = [
    path('notes/<slug:slug>/rate/', views.rate_note, name='rate-note'),
    path('notes/<slug:slug>/reviews/', views.note_reviews, name='note-reviews'),
    path('review/<int:pk>/delete/', views.delete_review, name='delete-review'),
] 