from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *
from random import randint
from django import forms


# Create your views here.
class NewMemberForm(forms.Form):
    STATUSCHOICES = (
    (1, ("ذكر")),
    (2, ("أنثى"))
)
    coustmerFirstName = forms.CharField(label="الأسم الأول", widget=forms.TextInput(attrs={'class': 'form-control'}))
    coustmerSurName = forms.CharField(label="الأسم الثاني" , widget=forms.TextInput(attrs={'class': 'form-control'}))
    coustomerMail = forms.EmailField(label="البريد الإلكتروني" , widget=forms.TextInput(attrs={'class': 'form-control'}))
    coustomerPhone = forms.CharField(label="رقم الهاتف", widget=forms.TextInput(attrs={'class': 'form-control'}))
    coustomerGender = forms.ChoiceField(choices= STATUSCHOICES, label="", widget=forms.Select(attrs={'class': 'form-control'}))
    
# The Index page
def index(request):
    if request.method == "GET":
        return render(request, "awardsapp/index.html", {
            "form" : NewMemberForm()
        })
    else:
        personFirstName = request.POST["coustmerFirstName"]
        personSurName = request.POST["coustmerSurName"]
        personEmail = request.POST["coustomerMail"]
        personPhone = request.POST["coustomerPhone"]
        personGender = request.POST["coustomerGender"]    
        personDoesHeKnow =  request.POST["buttonnory"]
        personFineorNot =  request.POST["fineornot"]
        personAgeGroup =  request.POST["theage"]   
        personCounter = 0
        
        isExist = Person.objects.filter(personPhone = personPhone)
        if not isExist:
            newPerson = Person.objects.create(personFineorNot=personFineorNot,personAgeGroup=personAgeGroup, personDoesHeKnow=personDoesHeKnow, personFirstName=personFirstName, personSurName=personSurName, personEmail=personEmail, personPhone=personPhone, personGender=personGender, personCounter=personCounter)
            return render(request, "awardsapp/index.html", {
                "form" : NewMemberForm(),
                "message" : f"لقد قمت بتسجيل بياناتك, انسخ الرابط التالي وشاركه مع اصدقائك لتفز!",
                "message2" : f"https://awards.mwatansuez.com/{personPhone}"
            })  
        else:
            return render(request, "awardsapp/index.html", {
                "form" : NewMemberForm(),
                "message" : f"هذا المشترك مسجل مسبقًا"
            })  

def countIn(request, personPhone):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else :
        ip = request.META.get('REMOTE_ADDR')
    isExist = Ips.objects.filter(theIp = ip)     
    if isExist:
        return HttpResponseRedirect(f"https://smarttargetkwt.com/")
    person = Person.objects.get(personPhone=personPhone)
    newCounter = person.personCounter + 1
    update = Person.objects.filter(personPhone=personPhone).update(personCounter=newCounter)
    newID = Ips.objects.create(theIp = ip)
    return HttpResponseRedirect(f"https://smarttargetkwt.com/")