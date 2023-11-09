from django.shortcuts import render, redirect

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

            return redirect('home')
    else:
        form = ToDoForm()
    
    context = {'form': form}

    return render(request, 'main/form.html', context)


def update_data(request, pk):
    data = ToDoStuff.objects.get(id=pk)
    form = ToDoForm(instance=data)

    if request.method == 'POST':
        form = ToDoForm(request.POST, instance=data)
        if form.is_valid():
            form.save()

        return redirect('home')

    context = {'form': form, 'data': data}

    return render(request, 'main/form.html', context)


def delete_data(request, pk):
    data = ToDoStuff.objects.get(id=pk)
    data.delete()

    return redirect('home')
