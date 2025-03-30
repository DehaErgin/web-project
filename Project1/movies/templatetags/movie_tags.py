from django import template
from django.db.models import Count

register = template.Library()

@register.filter
def get_rating_count(movie, score):
    """Get the count of ratings with a specific score for a movie"""
    return movie.ratings.filter(score=score).count()

@register.filter
def calculate_percentage(count, total):
    """Calculate the percentage of votes for a specific score"""
    if total == 0:
        return 0
    return (count / total) * 100 