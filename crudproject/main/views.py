from django.shortcuts import render

from .models import ToDoStuff
from .forms import ToDoForm


# Create your views here.
def home(request):
    data = ToDoStuff.objects.all()

    context = {'data': data}

    return render(request, 'main/todo.html', context)


def create_data(request):
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
    else:
        form = ToDoForm()
    
    context = {'form': form}

    return render(request, 'main/form.html', context)