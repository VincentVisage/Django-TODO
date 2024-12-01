from django.urls import path, include
from django.views.generic import TemplateView

from .views import (
    ToDoListIndexView,
    ToDoListView,
    ToDoListDoneView,
    ToDoDetailView,
    ToDoItemCreateView,
    ToDoItemUpdateView,
    ToDoItemDeleteView
)

app_name = "todo_list"

urlpatterns = [
    # path("", views.index_view, name='index'),
    # path("", ToDoListIndexView.as_view(), name='index'),
    path("", ToDoListIndexView.as_view(), name='index'),
    path('<int:pk>/', ToDoDetailView.as_view(), name='detail'),
    path("list/", ToDoListView.as_view(), name='list'),
    path('done/', ToDoListDoneView.as_view(), name='done'),
    path('create/', ToDoItemCreateView.as_view(), name='create'),
    path('<int:pk>/update/', ToDoItemUpdateView.as_view(), name='update'),
    path('<int:pk>/confirm-delete/', ToDoItemDeleteView.as_view(), name='delete'),
]