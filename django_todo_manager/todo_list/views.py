from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from .models import ToDoItem
from django.urls import reverse
# Create your views here.
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .forms import ToDoItemCreateForm, ToDoItemUpdateForm

def index_view(request: HttpRequest) -> HttpResponse:
    todo_items = ToDoItem.objects.order_by("id").all()
    return render(request, template_name='todo_list/index.html', context={'todo_items': todo_items})

class ToDoListIndexView(ListView):
    template_name = 'todo_list/index.html'
    # TODO: custom qs archived
    queryset = ToDoItem.objects.all()[:1]


class ToDoDetailView(DetailView):
    # TODO: archived qs
    queryset = ToDoItem.objects.filter(archived=False)

class ToDoListView(ListView):
    # model = ToDoItem
    queryset = ToDoItem.objects.filter(archived=False)


class ToDoListDoneView(ListView):
    # TODO: archived qs
    queryset = ToDoItem.objects.filter(done=True)


class ToDoItemCreateView(CreateView):
    model = ToDoItem
    form_class = ToDoItemCreateForm
    # fields = ('title', 'description')


class ToDoItemUpdateView(UpdateView):
    model = ToDoItem
    template_name_suffix = '_update_form'
    form_class = ToDoItemUpdateForm


class ToDoItemDeleteView(DeleteView):
    model = ToDoItem
    success_url = reverse_lazy('todo_list:list')

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.archived = True
        self.object.save()
        return HttpResponseRedirect(success_url)
