from django.contrib import admin
from django.urls import path
from .views import HomePageView , AboutPageView , SnacksListView , SnackDetailView , SnackCreateView , SnackUpdateView , SnackdeleteView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about', AboutPageView.as_view(), name='about'),
    path('snacksList', SnacksListView.as_view(), name='snacksList'),
    path('<int:pk>/', SnackDetailView.as_view(), name='snack_details'),
    path('create/', SnackCreateView.as_view(), name="snack_create"),
    path('update/<int:pk>',SnackUpdateView.as_view(), name="snack_update"),
    path('delete/<int:pk>',SnackdeleteView.as_view(), name="snack_delete"),

]