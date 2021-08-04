# Django Workshop Exercise 6

In this exercise we will expand the "CreatePerson" form from previous exercise to handle the senario where you want to modify the detail of an existing person.
<br/><br/>
## 1. Prepare for the coding environment  

SSH into the test machine. The password is 123456.
```sh
ssh your_upi@130.216.39.213
```
Once you are in, activate the python virtual environment and cd into the project folder
```sh
workon dj && cd mysite
```
<br/><br/>
## 2. Overwrite the constructor of the "CreatePerson" from class
Start  the server and go to the path "/main/createPerson". Notice that a "Save" button has been added to the form, and under the "Already Created" section an "Edit" link was added infront of each person entry. At the moment the "Save" button only submits an empty form no matter what you put in the fields, and the "Edit" link only redirect the user to the same page with the UPI parameter appended at the end of the url. The goal is to be populate the form with the person detail when the user click on the "Edit" link, and by clicking on the "Save" button, the corresponding person object is modified using the value from the fields of the form.

To populate the form with data, we need to overwrite the form's constructor to initialize the fields. Open the file "forms.py" and complete the consturctor for "CreatePerson" class.
<details>
  <summary>Click for solution</summary>
  
```sh
    def __init__(self, *args, **kwargs):
        person = kwargs.pop('person', Person(name="", upi="", isAdmin=False))
        super().__init__(*args, **kwargs)
        
        self.initial['name'] = person.name
        self.initial['upi'] = person.upi
        self.initial['isAdmin'] = person.isAdmin
```
</details>

<br/><br/>
## 3. Handle "Get" request from clicking the "Edit" link
When the user click on the "Edit" link from the "Already Created" section, it will take the user back to "/main/createPerson" using "Get", also the upi of the person is attached to the url as a parameter. Edit the function "createPerson" in "views.py", complete the "if request.method == "GET" branch. We want first find the person object with the upi equal to the upi parameter, then construct a "CreatePerson" form object using the person object.

<details>
  <summary>Click for solution</summary>
  
```sh
    if request.method == "GET":
        upi = request.GET.get('upi', "")
        #ToDo: Use the upi to find the corresponding person object in the database.
        #If the person is found then create the form using the Person object.
        #You can assume that every person in the database have a unique upi.
        p = Person.objects.filter(upi=upi)
        if p.count() == 1:
            form = CreatePerson(person = p[0])
```
</details>

If you implement everything correctly up to this point, clicking on the "Edit" link should populate the form with the data with the corresponding person detail.

<br/><br/>
## 4. Add logic for the "Save" button
When the user click on the "Save" button, the form will be submited to the current url using POST.  Then the Django's routing system will pass the request to the view function - "createPerson" in views.py.  Inside the view function,  complete the "if request.POST.get("save")" branch so that if the upi entered in the form belongs to one of the already created person objects, then update the the person object using the values from the form. 

<details>
  <summary>Click for solution</summary>
  
```sh
            if request.POST.get("save"): 
                #ToDo: If the upi entered in the form belongs to one of the already created person objects, 
                #then update the the person object using the values from the form.
                Person.objects.filter(upi=formData["upi"]).update(name=formData["name"],isAdmin=formData["isAdmin"])
                
                return HttpResponseRedirect("createPerson")
```
</details>
