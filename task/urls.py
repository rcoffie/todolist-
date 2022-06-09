from django.urls import path

from task import views

app_name = "task"

urlpatterns = [
    path("task-list/", views.task_list, name="task_list"),
    path("create-task/", views.create_task, name="create_task"),
    path("task-detail/<int:task_id>/", views.task_detail, name="task_detail"),
    path("update-task/<int:task_id>/", views.update_task, name="update_task"),
    path("delete-task/<int:task_id>/", views.delete_task, name="delete_task"),
]
