from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item, Person
from .forms import CreateList, CreatePerson, ShowItems

# Create your views here.
def index(request, id):
    ls = ToDoList.objects.get(id=id)
    if request.method == "POST":
        form = ShowItems(request.POST, ls=ls)
        if form.is_valid():
            if request.POST.get("save"):
                completenessList = form.cleaned_data["items"].values_list("id", flat=True)
                for item in ls.item_set.all():
                    if item.id in completenessList:
                        item.complete = True
                    else:
                        item.complete = False
                    item.save()

            elif request.POST.get("newItem"):
                text = request.POST.get("new")
                if len(text.strip()) > 0:
                    ls.item_set.create(text=text, complete=False)

        return HttpResponseRedirect(str(id))

    form = ShowItems(ls=ls)
    data = {
        "form": form,
        "ls": ls
    }
    return render(request, "main/list.html", data)


def home(request):
    ls = ToDoList.objects.all()
    return render(request, "main/home.html", {"list": ls})

def createList(request):
    if request.method == "POST":
        form = CreateList(request.POST)
        if form.is_valid():
            t = ToDoList(name=form.cleaned_data["name"])
            t.save()
        return HttpResponseRedirect("createList")


    form = CreateList()
    already_created = ToDoList.objects.all()
    data = {
            "create_title": "Create ToDoList",
            "form": form,
            "already_created": already_created
            }
    return render(request, "main/create.html", data)

def createPerson(request):
    if request.method == "POST":
        form = CreatePerson(request.POST)
        if form.is_valid():
            formData = form.cleaned_data
            if request.POST.get("create"):
                if Person.objects.filter(upi=formData["upi"]).count() == 0:
                    p = Person(name=formData["name"], upi=formData["upi"], isAdmin=formData["isAdmin"])
                    p.save()
                return HttpResponseRedirect("createPerson")

            if request.POST.get("save"):
                #ToDo: If the upi entered in the form belongs to one of the already created person objects, 
                #then update the the person object using the values from the form.
                Person.objects.filter(upi=formData["upi"]).update(name=formData["name"],isAdmin=formData["isAdmin"])
                
                return HttpResponseRedirect("createPerson")

    
    if request.method == "GET":
        upi = request.GET.get('upi', "")

        #ToDo: Use the upi to find the corresponding person object in the database.
        #If the person is found then create the form using the Person object.
        #You can assume that every person in the database have a unique upi.
        p = Person.objects.filter(upi=upi)
        if p.count() == 1:
            form = CreatePerson(person = p[0])


    if not 'form' in locals():
        form = CreatePerson()

    already_created = Person.objects.all()
    data = {
        "form": form,
        "create_title": "Manage Users",
        "already_created": already_created
    }
    return render(request, "main/person.html", data)
