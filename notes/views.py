from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.contrib import messages
from django.http import HttpResponse
from .models import Note, Subject, Comment
from django.urls import reverse_lazy

def home(request):
    return render(request, 'notes/home.html')

class NoteListView(ListView):
    model = Note
    template_name = 'notes/note_list.html'
    context_object_name = 'notes'
    paginate_by = 10
    
    def get_queryset(self):
        return Note.objects.filter(approved=True, is_private=False).order_by('-uploaded_at')

class NoteDetailView(DetailView):
    model = Note
    template_name = 'notes/note_detail.html'

class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    template_name = 'notes/note_form.html'
    fields = ['title', 'description', 'subject', 'semester', 'file', 'tags', 'is_private']
    success_url = reverse_lazy('note-list')
    
    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        return super().form_valid(form)

class NoteUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Note
    template_name = 'notes/note_form.html'
    fields = ['title', 'description', 'subject', 'semester', 'file', 'tags', 'is_private']
    
    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        note = self.get_object()
        return self.request.user == note.uploaded_by

class NoteDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Note
    success_url = reverse_lazy('note-list')
    template_name = 'notes/note_confirm_delete.html'
    
    def test_func(self):
        note = self.get_object()
        return self.request.user == note.uploaded_by

class MyNotesListView(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'notes/my_notes.html'
    context_object_name = 'notes'
    paginate_by = 10
    
    def get_queryset(self):
        return Note.objects.filter(uploaded_by=self.request.user).order_by('-uploaded_at')

class BookmarkedNotesListView(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'notes/bookmarked_notes.html'
    context_object_name = 'notes'
    paginate_by = 10
    
    def get_queryset(self):
        return self.request.user.bookmarked_notes.all().order_by('-uploaded_at')

@login_required
def note_download(request, slug):
    note = get_object_or_404(Note, slug=slug)
    if note.is_private and note.uploaded_by != request.user:
        messages.error(request, 'This note is private.')
        return redirect('note-list')
    note.download_count += 1
    note.save()
    response = HttpResponse(note.file, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename="{note.file.name}"'
    return response

@login_required
def toggle_bookmark(request, slug):
    note = get_object_or_404(Note, slug=slug)
    if request.user in note.bookmarked_by.all():
        note.bookmarked_by.remove(request.user)
        messages.success(request, 'Note removed from bookmarks.')
    else:
        note.bookmarked_by.add(request.user)
        messages.success(request, 'Note added to bookmarks.')
    return redirect('note-detail', slug=slug)

@login_required
def add_comment(request, slug):
    note = get_object_or_404(Note, slug=slug)
    if request.method == 'POST':
        content = request.POST.get('content')
        parent_id = request.POST.get('parent_id')
        if content:
            comment = Comment(note=note, user=request.user, content=content)
            if parent_id:
                comment.parent_id = parent_id
            comment.save()
            messages.success(request, 'Comment added successfully.')
    return redirect('note-detail', slug=slug)

@login_required
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.user == comment.user:
        comment.delete()
        messages.success(request, 'Comment deleted successfully.')
    return redirect('note-detail', slug=comment.note.slug)

class SubjectListView(ListView):
    model = Subject
    template_name = 'notes/subject_list.html'
    context_object_name = 'subjects'

class SubjectDetailView(DetailView):
    model = Subject
    template_name = 'notes/subject_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['notes'] = Note.objects.filter(
            subject=self.object,
            approved=True,
            is_private=False
        ).order_by('-uploaded_at')
        return context 