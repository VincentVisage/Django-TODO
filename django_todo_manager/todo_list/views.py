from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import ToDoItem
from django.urls import reverse
# Create your views here.
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .forms import ToDoItemForm

def index_view(request: HttpRequest) -> HttpResponse:
    todo_items = ToDoItem.objects.order_by("id").all()
    return render(request, template_name='todo_list/index.html', context={'todo_items': todo_items})

class ToDoListIndexView(ListView):
    template_name = 'todo_list/index.html'
    queryset = ToDoItem.objects.all()[:1]


class ToDoDetailView(DetailView):
    model = ToDoItem

class ToDoListView(ListView):
    model = ToDoItem


class ToDoListDoneView(ListView):
    model = ToDoItem
    queryset = ToDoItem.objects.filter(done=True).all()

class ToDoItemCreateView(CreateView):
    model = ToDoItem
    form_class = ToDoItemForm
    # fields = ('title', 'description')
