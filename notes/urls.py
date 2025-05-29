from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('notes/', views.NoteListView.as_view(), name='note-list'),
    path('notes/upload/', views.NoteCreateView.as_view(), name='note-upload'),
    path('notes/<slug:slug>/', views.NoteDetailView.as_view(), name='note-detail'),
    path('notes/<slug:slug>/edit/', views.NoteUpdateView.as_view(), name='note-edit'),
    path('notes/<slug:slug>/delete/', views.NoteDeleteView.as_view(), name='note-delete'),
    path('notes/<slug:slug>/download/', views.note_download, name='note-download'),
    path('my-notes/', views.MyNotesListView.as_view(), name='my-notes'),
    path('notes/<slug:slug>/bookmark/', views.toggle_bookmark, name='toggle-bookmark'),
    path('bookmarks/', views.BookmarkedNotesListView.as_view(), name='bookmarked-notes'),
    path('notes/<slug:slug>/comment/', views.add_comment, name='add-comment'),
    path('comment/<int:pk>/delete/', views.delete_comment, name='delete-comment'),
    path('subjects/', views.SubjectListView.as_view(), name='subject-list'),
    path('subjects/<slug:slug>/', views.SubjectDetailView.as_view(), name='subject-detail'),
] 