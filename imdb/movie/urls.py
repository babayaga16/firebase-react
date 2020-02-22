from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from .import views
from .views import MovieList , Moviedetail , MovieCategory,MovieLanguage,MovieYear,search
app_name = 'movie'
urlpatterns = [
    path('', MovieList.as_view(), name='movie_list'),
    path('<slug:slug>/', Moviedetail.as_view(), name='movie_detail'),
    path('category/<str:category>/', MovieCategory.as_view(), name='movie_category'),
    path('search/', views.search, name='movie_search'),
    path('language/<str:lang>/', MovieLanguage.as_view(), name='movie_language'),
    path('year/<int:year>' ,MovieYear.as_view() ,name ='movie_year')
]