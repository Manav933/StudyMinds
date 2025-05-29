from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from notes.models import Note
from .models import Rating

@login_required
def rate_note(request, slug):
    note = get_object_or_404(Note, slug=slug)
    if request.method == 'POST':
        stars = request.POST.get('stars')
        review = request.POST.get('review', '')
        
        if stars:
            rating, created = Rating.objects.get_or_create(
                note=note,
                user=request.user,
                defaults={'stars': stars, 'review': review}
            )
            
            if not created:
                rating.stars = stars
                rating.review = review
                rating.save()
            
            messages.success(request, 'Your rating has been saved!')
        else:
            messages.error(request, 'Please provide a star rating.')
    
    return redirect('note-detail', slug=slug)

@login_required
def note_reviews(request, slug):
    note = get_object_or_404(Note, slug=slug)
    reviews = Rating.objects.filter(note=note).order_by('-created_at')
    return render(request, 'ratings/note_reviews.html', {
        'note': note,
        'reviews': reviews
    })

@login_required
def delete_review(request, pk):
    review = get_object_or_404(Rating, pk=pk)
    if request.user == review.user:
        note_slug = review.note.slug
        review.delete()
        messages.success(request, 'Your review has been deleted.')
        return redirect('note-detail', slug=note_slug)
    messages.error(request, 'You can only delete your own reviews.')
    return redirect('note-detail', slug=review.note.slug) 