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
Start  the server and go to the path /main/createPerson. Notice that a new "Save" button has been added to the form, and under the "Already Created" section an "Edit" link was added infront of each person entry. At the moment the "Save" button only submits an empty form no matter what you put in the fields, and the "Edit" link redirect the user back to the same page with the UPI parameter appended at the end of the url. The goal is to be populate the form with the person detail when the user click on the "Edit" link, and by clicking on the "Save" button, the corresponding person object is modified using the value from the fields of the form.

