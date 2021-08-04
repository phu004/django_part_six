from django import forms
from .models import Item, Person

class CreateList(forms.Form):
    name=forms.CharField(max_length=200)
    check=forms.BooleanField(required=False)

class ShowItems(forms.Form):
    items = forms.ModelMultipleChoiceField(label="", required=False, widget = forms.CheckboxSelectMultiple, queryset=None)

    def __init__(self, *args, **kwargs):
        ls = kwargs.pop('ls', None)
        super().__init__(*args, **kwargs)
        self.fields['items'].queryset = Item.objects.filter(todolist_id=ls.id)
        self.initial['items'] = [item.id for item in Item.objects.filter(complete=True)]


class CreatePerson(forms.Form):
    name = forms.CharField(max_length=200)
    upi = forms.CharField(max_length=10, label="UPI")
    isAdmin = forms.BooleanField(label="Admin Priviliege", required=False)

    def __init__(self, *args, **kwargs):
        person = kwargs.pop('person', Person(name="", upi="", isAdmin=False))
        super().__init__(*args, **kwargs)
        
        #ToDo: You can assume that a Person object (under the name "person") will be passed into this constructor.
        # Use the data in the Person object to initilize the fields of the form.
        self.initial['name'] = person.name
        self.initial['upi'] = person.upi
        self.initial['isAdmin'] = person.isAdmin
        
    