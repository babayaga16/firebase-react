from django.shortcuts import render
from django.db.models import Q
from django.views.generic import ListView , DetailView
from .models import Movie,MovieLink
from django.views.generic.dates import YearArchiveView


class MovieList(ListView):
    model = Movie
    paginate_by = 3





# Create your views here.

class Moviedetail(DetailView):
    model = Movie


    def get_object(self):
        object = super(Moviedetail , self).get_object()
        object.views_count += 1
        object.save()
        return object

    def get_context_data(self, **kwargs):
        context = super(Moviedetail, self).get_context_data(**kwargs)
        context['links'] = MovieLink.objects.filter(movie = self.get_object())
        context['related'] = Movie.objects.filter(category = self.get_object().category)
        return context

class MovieCategory(ListView):
    model = Movie
    paginate_by = 3

    def get_queryset(self):
        self.category = self.kwargs['category']
        return Movie.objects.filter(category =self.category)

    def get_context_data(self, **kwargs):
        context = super(MovieCategory, self).get_context_data(**kwargs)
        context['movie_category'] =self.category
        return context

class MovieLanguage(ListView):
    model = Movie
    paginate_by = 3
    def get_queryset(self):
        self.language = self.kwargs['lang']
        return Movie.objects.filter(language =self.language)

    def get_context_data(self, **kwargs):
        context = super(MovieLanguage, self).get_context_data(**kwargs)
        context['movie_language'] =self.language
        return context


class MovieYear(YearArchiveView):
    queryset = Movie.objects.all()
    date_field = 'year'
    make_object_list = True
    allow_future = True


def search (request):
    movie = Movie.objects.all()
    search_term = ''

    if 'query' in request.GET:
     search_term = request.GET['query']
     object_list = movie.objects.filter(title__icontains =search_term)

    context = {'object_list':object_list}
    return render(request , 'movie/search_result.html',context)

