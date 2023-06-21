from django.urls import path
from . import views
urlpatterns = [
    path("", views.task_list,name="task_list"),
    path("edit/<int:task_id>/", views.edit_task,name="edit_task"),
    path("delete/<int:task_id>/", views.delete_task,name="delete_task"),
    path("create_task/", views.create_task,name="create_task"),
    path("manager_dash/", views.manager_dash,name='manager_dash'),
    path("employee_list/<int:userid>/", views.employee_list,name='employee_list'),

]
