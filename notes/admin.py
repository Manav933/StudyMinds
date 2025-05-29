from django.contrib import admin
from .models import Subject, Note, Download, Comment

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'course')
    search_fields = ('name', 'course')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject', 'uploaded_by', 'approved', 'download_count', 'uploaded_at')
    list_filter = ('approved', 'subject', 'semester')
    search_fields = ('title', 'description', 'uploaded_by__username')
    prepopulated_fields = {'slug': ('title',)}
    actions = ['approve_notes', 'unapprove_notes']
    
    def approve_notes(self, request, queryset):
        queryset.update(approved=True)
    approve_notes.short_description = "Approve selected notes"
    
    def unapprove_notes(self, request, queryset):
        queryset.update(approved=False)
    unapprove_notes.short_description = "Unapprove selected notes"

@admin.register(Download)
class DownloadAdmin(admin.ModelAdmin):
    list_display = ('note', 'user', 'downloaded_at')
    list_filter = ('downloaded_at',)
    search_fields = ('note__title', 'user__username')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('note', 'user', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('note__title', 'user__username', 'content') 