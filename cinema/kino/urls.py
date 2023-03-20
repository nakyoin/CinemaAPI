from django.urls import path
from . import views

urlpatterns = [
    path('', views.FilmApiView.as_view()),
    path('<int:pk>/', views.SingleFilmView.as_view()),

]