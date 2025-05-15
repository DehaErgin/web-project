from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404
from django.db.models import Q
from .models import Movie, UserList, Comment, Rating, MovieList

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/dashboard/')
    return render(request, 'movies/index.html')

def custom_login(request):
    # Clear existing messages
    storage = messages.get_messages(request)
    for message in storage:
        pass  # Mark all messages as read
    storage.used = True  # Mark the storage as used
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    
    return render(request, 'registration/login.html', {'form': form})

def register(request):
    # Clear existing messages
    storage = messages.get_messages(request)
    for message in storage:
        pass  # Mark all messages as read
    storage.used = True  # Mark the storage as used
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('dashboard')
        else:
            for error in form.errors.values():
                messages.error(request, error)
    else:
        form = UserCreationForm()
    
    return render(request, 'registration/register.html', {'form': form})

@login_required
def dashboard(request):
    # Get user's movie lists - use the appropriate model
    user_lists = UserList.objects.filter(user=request.user)
    movie_lists = MovieList.objects.filter(user=request.user)
    
    context = {
        'user_lists': user_lists,
        'movie_lists': movie_lists
    }
    
    return render(request, 'movies/dashboard.html', context)

@login_required
def movies(request):
    # Get all movie years and directors for filtering
    years = Movie.objects.values_list('year', flat=True).distinct().order_by('-year')
    directors = Movie.objects.values_list('director', flat=True).distinct().order_by('director')
    
    # Get all movies with filtering
    all_movies = Movie.objects.all()
    
    # Apply search filter
    search_query = request.GET.get('search')
    if search_query:
        all_movies = all_movies.filter(
            Q(title__icontains=search_query) | 
            Q(description__icontains=search_query) |
            Q(director__icontains=search_query)
        )
    
    # Apply year filter
    year_filter = request.GET.get('year')
    if year_filter:
        all_movies = all_movies.filter(year=year_filter)
    
    # Apply director filter
    director_filter = request.GET.get('director')
    if director_filter:
        all_movies = all_movies.filter(director=director_filter)
    
    # Get user's lists for the dropdown
    user_lists = UserList.objects.filter(user=request.user)
    movie_lists = MovieList.objects.filter(user=request.user)
    
    context = {
        'movies': all_movies,
        'user_lists': user_lists,
        'movie_lists': movie_lists,
        'years': years,
        'directors': directors
    }
    
    return render(request, 'movies/movies.html', context)

@login_required
def create_list(request):
    if request.method == 'POST':
        list_name = request.POST.get('list_name')
        if list_name:
            # Create a new list
            user_list = UserList.objects.create(
                name=list_name,
                user=request.user
            )
            messages.success(request, f'List "{list_name}" created successfully!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Please provide a name for your list.')
    return render(request, 'movies/create_list.html')

@login_required
def add_to_list(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    
    # Get user's lists or create default list if none exists
    user_lists = UserList.objects.filter(user=request.user)
    
    if not user_lists.exists():
        # Create a default list for the user
        default_list = UserList.objects.create(
            name="My Favorites",
            user=request.user
        )
        default_list.movies.add(movie)
        messages.success(request, f'Added "{movie.title}" to your new list "My Favorites"!')
    else:
        # Add to the first list (in a real app, you'd let users choose which list)
        default_list = user_lists.first()
        default_list.movies.add(movie)
        messages.success(request, f'Added "{movie.title}" to your list "{default_list.name}"!')
    
    return redirect('movies')

@login_required
def add_to_specific_list(request, movie_id, list_id):
    movie = get_object_or_404(Movie, id=movie_id)
    # Try to get the list from UserList first
    try:
        user_list = UserList.objects.get(id=list_id, user=request.user)
        user_list.movies.add(movie)
        messages.success(request, f'Added "{movie.title}" to your list "{user_list.name}"!')
        return redirect('movies')
    except UserList.DoesNotExist:
        # If not found in UserList, try MovieList
        try:
            movie_list = MovieList.objects.get(id=list_id, user=request.user)
            movie_list.movies.add(movie)
            messages.success(request, f'Added "{movie.title}" to your list "{movie_list.name}"!')
            return redirect('movies')
        except MovieList.DoesNotExist:
            raise Http404("List not found")

@login_required
def delete_list(request, list_id):
    user_list = get_object_or_404(UserList, id=list_id, user=request.user)
    list_name = user_list.name
    user_list.delete()
    messages.success(request, f'List "{list_name}" has been deleted.')
    return redirect('dashboard')

@login_required
def view_list(request, list_id):
    # Try to get the list from UserList first
    try:
        user_list = UserList.objects.get(id=list_id)
        return render(request, 'movies/view_list.html', {
            'user_list': user_list,
            'is_own_list': user_list.user == request.user
        })
    except UserList.DoesNotExist:
        # If not found in UserList, try MovieList
        try:
            movie_list = MovieList.objects.get(id=list_id)
            return render(request, 'movies/view_list.html', {
                'user_list': movie_list,
                'is_own_list': movie_list.user == request.user
            })
        except MovieList.DoesNotExist:
            raise Http404("List not found")

@login_required
def remove_from_list(request, list_id, movie_id):
    # Try to get the list from UserList first
    try:
        user_list = UserList.objects.get(id=list_id, user=request.user)
        movie = get_object_or_404(Movie, id=movie_id)
        user_list.movies.remove(movie)
        messages.success(request, f'Removed "{movie.title}" from your list "{user_list.name}".')
        return redirect('view_list', list_id=list_id)
    except UserList.DoesNotExist:
        # If not found in UserList, try MovieList
        try:
            movie_list = MovieList.objects.get(id=list_id, user=request.user)
            movie = get_object_or_404(Movie, id=movie_id)
            movie_list.movies.remove(movie)
            messages.success(request, f'Removed "{movie.title}" from your list "{movie_list.name}".')
            return redirect('view_list', list_id=list_id)
        except MovieList.DoesNotExist:
            raise Http404("List not found")

@login_required
def movie_comments(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    comments = movie.comments.all()
    
    if request.method == 'POST':
        text = request.POST.get('comment_text')
        if text:
            Comment.objects.create(
                movie=movie,
                user=request.user,
                text=text
            )
            messages.success(request, 'Comment added successfully!')
            return redirect('movie_comments', movie_id=movie.id)
    
    return render(request, 'movies/movie_comments.html', {
        'movie': movie,
        'comments': comments
    })

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    
    # Only the comment author can delete their comment
    if comment.user != request.user:
        messages.error(request, "You cannot delete someone else's comment!")
        return redirect('movie_comments', movie_id=comment.movie.id)
    
    movie_id = comment.movie.id
    comment.delete()
    messages.success(request, 'Comment deleted successfully!')
    return redirect('movie_comments', movie_id=movie_id)

@login_required
def rate_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    
    if request.method == 'POST':
        score = request.POST.get('score')
        comment = request.POST.get('comment', '')
        
        if score:
            # Check if user already rated this movie
            rating, created = Rating.objects.update_or_create(
                movie=movie,
                user=request.user,
                defaults={'score': score, 'comment': comment}
            )
            
            if created:
                messages.success(request, f'You rated {movie.title} with {score}/10')
            else:
                messages.success(request, f'Your rating for {movie.title} has been updated')
                
            # Redirect back to the movie details page
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            return redirect('movies')
    
    # If GET request, show the rating form
    context = {
        'movie': movie,
        'existing_rating': Rating.objects.filter(movie=movie, user=request.user).first()
    }
    return render(request, 'movies/rate_movie.html', context)

@login_required
def view_ratings(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    ratings = movie.ratings.all()
    
    # Check if the current user has rated this movie
    user_rating = None
    if request.user.is_authenticated:
        user_rating = Rating.objects.filter(movie=movie, user=request.user).first()
    
    context = {
        'movie': movie,
        'ratings': ratings,
        'user_rating': user_rating
    }
    return render(request, 'movies/view_ratings.html', context)
