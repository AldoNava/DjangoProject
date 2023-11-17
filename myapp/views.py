from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render, redirect
import lorem
from .forms import CreateNewTask, CreateNewProject
# Create your views here.
def index(request):
    text = lorem.text()
    return render(request, 'index.html', {
        'text': text
    })

def hello(request, username=None):
    return HttpResponse('Hello %s ' %username)

def about(request):
    username = 'Aldo'
    return render(request, 'about.html', {
        'username': username
    })

def projects(request):
    projects = list(Project.objects.all().values())
    print(projects)
    #return JsonResponse(projects, safe=False)
    return render(request, 'project.html', {
        'projects': projects
    })

def tasks(request):
    #task = Task.objects.get(id=id)
    #task = get_object_or_404(Task, id=id)
    #return HttpResponse('task: %s'  % task.title)
    tasks = Task.objects.all()
    return render(request, 'tasks.html', {
        'tasks': tasks
    })

def create_task(request):
    if request.method == 'GET':
        return render(request, 'create_task.html', {
            'form': CreateNewTask
        })
    else:
        Task.objects.create(title=request.POST['title'], description=request.POST['description'], project_id=2)
        return redirect('tasks')


def create_project(request):
    if request.method == 'GET':
        return render(request, 'create_project.html', {
            'form': CreateNewProject
        })
    else:
        Project.objects.create(name=request.POST['name'])
        return redirect('projects')

def project_detail(request, id):
    #Project.objects.get(id=id)
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filer(project_id=id)
    return render(request, 'detail.html', {
        'proj': project,
        'tasks': tasks
    })