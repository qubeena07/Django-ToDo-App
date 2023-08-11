from django.urls import path
from . import views

urlpatterns = [
    path('addTask/',views.addTask,name="addTask"),

    #mark as done
    path('mark_as_done/<int:pk>/',views.mark_as_done,name="mark_as_done"),
    #edit
    path('edit_task/<int:pk>/',views.edit_task,name="edit_task"),

    #delete task
    path('delete_task/<int:pk>/',views.delete_task,name="delete_task"),

]