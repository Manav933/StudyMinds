from django.contrib import admin
from .models import Rating

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('note', 'user', 'stars', 'created_at')
    list_filter = ('stars', 'created_at')
    search_fields = ('note__title', 'user__username', 'review') 