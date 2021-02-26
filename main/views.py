from audioop import reverse
from urllib import request
from urllib.request import Request

from django.http.response import HttpResponseRedirect
from main.forms import TaskForm
from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm



def index(request):
    tasks = Task.objects.all()
    return render(request, 'main/index.html', {'title': 'Main page', 'tasks': tasks})


def speak(request):
    return render(request, 'main/speak.html')

def tts(request):
    return render(request, 'main/tts.html')    




def create(request):
    error = ''
    if request.method == 'POST':
        form =TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Invalid data'


    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)

