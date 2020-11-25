from django.shortcuts import render, redirect
from myApp.models import Movies


# Create your views here.

def home(request):
    return render(request,'myApp/home.html')

def addMovies(request):
    return render(request, 'myApp/addMovies.html')

def about(request):
    return render(request, 'myApp/about.html')

"""def complainView(request):
    return render(request, 'myApp/complainView.html')"""

def add(request):
    """
    Process request to add new item to the inventory.  Return back to the 
    main index page when done.
    """
    # Read values from GET request (TODO: Add error checking here)
    #try:
    movie_name = request.GET["movie_name"]
    movie_type = request.GET["movie_type"]
    movies_characters = request.GET["movies_characters"]
    language = request.GET["language"]
    released_country = request.GET["released_country"]
    released_date = request.GET["released_date"]
    # Save to the database
    movies = Movies(movie_name=movie_name, movie_type=movie_type, 
                movies_characters=movies_characters, language=language,
                released_country=released_country,released_date=released_date )
    movies.save()
    """
    except Exception as e:
        # TODO: Send an error message back to the main index page
        print("Unable to save to database: {}".format(e))
    """
    # Return to main index page
    return redirect("home")
def viewMovies(request):
    """
    Display only the details of the item_id specified.
    """
    # Get the item based on the item_id
    movies = Movies.objects.all()

    # Build the dictionary of parameters for the HTML template
    values = {"movies" : movies}

    # Create and display the HTML page
    return render(request, 'myApp/viewMovies.html', values)