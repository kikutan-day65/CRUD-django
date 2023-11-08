from django.shortcuts import render

from .models import ToDoStuff
from .forms import ToDoForm


# Create your views here.
def home(request):
    return render(request, 'main/todo.html')


def create_data(request):
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            print("POSTed succeesfully!")
    else:
        form = ToDoForm()
    
    context = {'form': form}

    return render(request, 'main/form.html', context)