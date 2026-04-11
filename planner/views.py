from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json
from .models import User, Task, Circle, Membership

# Create your views here
def index(request):
    return render(request, 'planner/index.html')

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "planner/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "planner/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "planner/register.html")

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "planner/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "planner/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

# All of user's tasks from all circles
def activity(request):
    user = request.user
    tasks = Task.objects.filter(assigned_to = user)
    return render(request, "planner/activity.html", {"tasks": tasks})

# All circles 
def circles(request):
    user = request.user
    memberships = Membership.objects.filter(user=request.user).select_related('circle', 'circle__created_by')

    return render(request, "planner/circles.html", {"memberships": memberships})

# Individual circle
def circle(request, c_id):
    circle = get_object_or_404(Circle, id = c_id)
    form_type = request.GET.get("type")
    is_admin = Membership.objects.filter(
    user=request.user,
    circle=circle,
    role='admin'
    ).exists()

    tasks = circle.tasks.all()

    return render(request, "planner/circle.html", 
    {"circle": circle, "tasks": tasks, "form_type": form_type, "is_admin":is_admin})

# User's  tasks in a circle
def my_tasks(request, c_id):
    circle = get_object_or_404(Circle, id = c_id)

    tasks = circle.tasks.filter(assigned_to = request.user)

    return render(request, "planner/circle.html", {"tasks": tasks, "circle": circle})

# Join a circle
def join(request):
    if request.method == "POST":
        c_id = request.POST.get("c_id")

        circle = get_object_or_404(Circle, id = c_id)
        Membership.objects.get_or_create(
            user = request.user,
            circle = circle,
        )

        return redirect("circles")

    return render(request, "planner/circles.html", {
        "form_type": "join"
    })

# Create a new circle
def create(request):
    if request.method == "POST":
        name = request.POST.get("c_name")

        circle = Circle.objects.create(name = name, created_by = request.user)
        Membership.objects.create(
            user = request.user,
            circle = circle,
            role = 'admin'
        )

        return redirect("circles")
    
    return render(request, "planner/circles.html", {
        "form_type": "create"
    })

# Exit a circle
def exit(request):
    user = request.user

    circles = Circle.objects.filter(memberships__user = user).values('id', 'name').distinct()

    if request.method == "POST":
        circle_id = request.POST.get("c_id")

        Membership.objects.filter(user=user, circle_id=circle_id).delete()

        return redirect("circles")

    return render(request, "planner/exit.html", {
        "circles": circles})

def delete(request):
    user = request.user

    circles = Circle.objects.filter(memberships__user = user, memberships__role = 'admin').values('id', 'name').distinct()

    if request.method == "POST":
        circle_id = request.POST.get("c_id")

        Circle.objects.filter(id=circle_id, memberships__user=user, memberships__role='admin').delete()

        return redirect("circles")

    return render(request, "planner/delete.html", {
        "circles": circles})

def assign_tasks(request, c_id):
    circle = get_object_or_404(Circle, id=c_id)

    if request.method == "POST":
        title = request.POST.get("title")
        desc = request.POST.get("desc")
        assigned_to_id = request.POST.get("assigned_to")
        due_date = request.POST.get("due_date")

        assigned_user = get_object_or_404(User, id=assigned_to_id)

        Task.objects.create(
            circle=circle,
            title=title,
            desc=desc,
            assigned_to=assigned_user,
            due_date=due_date
        )

        return redirect("circle", c_id=circle.id)

    members = User.objects.filter(membership__circle=circle)
    return render(request, "planner/assign_tasks.html", {"circle": circle, "members": members})

def toggle_task(request, task_id):
    if request.method == "POST":
        task = get_object_or_404(Task, id = task_id)

        user = request.user
        if task.assigned_to != user:
            return JsonResponse({
                "error": "Unauthorised"
            }, status = 403)

        if task.status == Task.TODO:
            task.status = Task.DONE
        else:
            task.status = Task.TODO

        task.save()

        return JsonResponse({"status": task.status})