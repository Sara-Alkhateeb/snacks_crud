from django.shortcuts import render
from django.views.generic import TemplateView , ListView , DetailView , CreateView , UpdateView , DeleteView
from .models import Snack
from django.urls import reverse_lazy

# Create your views here.
class HomePageView(TemplateView):
    template_name='home.html'

class AboutPageView(TemplateView):
    template_name='about.html'

class SnacksListView(ListView):
    template_name='snack_list.html'
    model = Snack

class SnackDetailView(DetailView):
    template_name='snack_detail.html'
    model=Snack

class SnackCreateView(CreateView):
     template_name='snack_creat.html'
     model=Snack
     fields= ['name', 'description', 'purchaser']

class SnackUpdateView(UpdateView):
    template_name='snack_update.html'
    model=Snack
    fields="__all__"
    success_url=reverse_lazy('snacksList')

class SnackdeleteView(DeleteView):
    template_name='snack_delete.html'
    model=Snack
    success_url=reverse_lazy('snacksList')