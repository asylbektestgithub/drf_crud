from django.urls import path
from .views import (
    my_api_view,
    tasklist_view,
    task_detail_view,
    task_create_view

)

urlpatterns = [
    path('', my_api_view),
    path('tasks/', tasklist_view),
    path('task-detail/<int:id>/', task_detail_view),
    path('task-create/', task_create_view),

]
