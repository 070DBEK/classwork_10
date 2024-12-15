from django.shortcuts import render, get_object_or_404, redirect
from .models import Task


def task_list(request):
    tasks = Task.objects.all()
    ctx = {'tasks': tasks}
    return render(request, 'tasks/list.html', ctx)


def create_task(request):
    if request.method == "POST":
        task_title = request.POST.get('task_title')
        due_date = request.POST.get('due_date')
        description = request.POST.get('description')
        if task_title and due_date and description:
            Task.objects.create(
                task_title=task_title,
                due_date=due_date,
                description=description,
            )
            return redirect('tasks:list')
    return render(request, 'tasks/form.html')


def update_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == "POST":
        task_title = request.POST.get('task_title')
        due_date = request.POST.get('due_date')
        description = request.POST.get('description')
        if task_title and due_date and description:
            task.task_title = task_title
            task.due_date = due_date
            task.due_date = due_date
            return redirect(task.get_detail_url())
    ctx = {'task': task}
    return render(request, 'tasks/form.html', ctx)


def task_detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    ctx = {'task': task}
    return render(request, 'tasks/detail.html', ctx)


def task_delete(request, task_id):
        task = get_object_or_404(Task, pk=task_id)
        task.delete()
        return redirect('tasks:list')