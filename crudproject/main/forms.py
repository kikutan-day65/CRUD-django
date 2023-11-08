from django.forms import ModelForm
from .models import ToDoStuff


class ToDoForm(ModelForm):
    class Meta:
        model = ToDoStuff
        fields = [
            'stuff',
            'detail',
        ]
        