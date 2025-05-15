from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from movies.models import Movie, Rating, MovieList, UserList

def member_list(request):
    members = User.objects.all().order_by('username')
    # Add total list counts for each member
    for member in members:
        movie_lists_count = member.movie_lists.count()
        user_lists_count = UserList.objects.filter(user=member).count()
        member.total_lists = movie_lists_count + user_lists_count
    return render(request, 'members/member_list.html', {'members': members})

def member_detail(request, username):
    user = get_object_or_404(User, username=username)
    ratings = Rating.objects.filter(user=user).order_by('-created_at')[:5]
    movie_lists = user.movie_lists.all()  # Using related_name from MovieList model
    user_lists = UserList.objects.filter(user=user)
    
    # Calculate total lists
    total_lists = len(movie_lists) + len(user_lists)
    
    # Get the current user's lists for comparison
    current_user_lists = []
    if request.user.is_authenticated:
        current_user_lists = list(UserList.objects.filter(user=request.user).values_list('id', flat=True))
        current_user_lists.extend(list(MovieList.objects.filter(user=request.user).values_list('id', flat=True)))
    
    context = {
        'profile_user': user,
        'ratings': ratings,
        'movie_lists': movie_lists,
        'user_lists': user_lists,
        'current_user_lists': current_user_lists,
        'is_own_profile': request.user == user,
        'total_lists': total_lists
    }
    return render(request, 'members/member_detail.html', context)

def member_reviews(request, username):
    user = get_object_or_404(User, username=username)
    ratings = Rating.objects.filter(user=user).order_by('-created_at')
    
    context = {
        'profile_user': user,
        'ratings': ratings,
    }
    return render(request, 'members/member_reviews.html', context)
