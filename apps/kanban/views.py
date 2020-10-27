from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import Kanban


class KanbanHomePage(LoginRequiredMixin, ListView):
    model = Kanban
    template_name = 'kanban/home.html'
    context_object_name = 'tables'
