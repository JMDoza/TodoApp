from django.shortcuts import render, redirect
from .models import Todo
from .forms import UpdateForm

# Create your views here.
def index(request):
    tasks = Todo.objects.all()
    context = {'tasks': tasks}
    if request.method == 'POST':
        if request.POST.get('task'):
            task = request.POST.get('task')
            Todo.objects.create(task_name=task)
            return redirect('index')
        elif request.POST.get('completed'):
            id = request.POST.get('completed')
            Todo.objects.filter(id=id).update(completed=1)
            return redirect('index')
    else:
        return render(request, 'Todo/index.html', context)

def update_task(request, id):
    task = Todo.objects.get(id=id)
    form = UpdateForm(request.POST or None, instance=task)

    if form.is_valid():
        form.save()
        return redirect('index')

    return render(request, 'Todo/update.html', {'form':form})

def delete_task(request, id):
    task = Todo.objects.get(id=id)

    if request.method == 'POST':
        task.delete()
        return redirect('index')

    return render(request, 'Todo/delete.html', {'task': task})