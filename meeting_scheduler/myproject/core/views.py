from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import *


class HomeView(ListView):
    model = Room
    template_name = 'core/home.html'


class RoomView(DetailView):
    model = Room
    template_name = 'core/room.html'
