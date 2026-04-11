from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("activity", views.activity, name="activity"),
    path("circles", views.circles, name="circles"),
    path("join", views.join, name="join"),
    path("create", views.create, name="create"),
    path("exit", views.exit, name="exit"),
    path("delete", views.delete, name="delete"),
    path("circle/<int:c_id>/", views.circle, name="circle"),
    path("my_tasks/<int:c_id>/", views.my_tasks, name="my_tasks"),
    path("assign_tasks/<int:c_id>/", views.assign_tasks, name="assign_tasks"),
    path("task/<int:task_id>/toggle/", views.toggle_task, name="toggle_task")
]