from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth                 
from django.template.context_processors import csrf 
from form import patientRegForm
from django.utils import timezone
from .models import toDoList, patient, case
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .form import toDoListForm, openCaseForm
from rest_framework import viewsets
from .serializers import toDoListSerializer, patientSerializer, caseSerializer
import json

#For API
class toDoListViewSet(viewsets.ModelViewSet):
    queryset = toDoList.objects.all()
    serializer_class = toDoListSerializer
    
class patientViewSet(viewsets.ModelViewSet):
    queryset = patient.objects.all()
    serializer_class = patientSerializer

class caseViewSet(viewsets.ModelViewSet):
    queryset = case.objects.all()
    serializer_class = caseSerializer

#For Webapp
@login_required
def dashboard(request):
	#Clear previous patienId
    if 'patientId' in request.session:
        del request.session['patientId']

    #Get user todo list
    posts = toDoList.objects.filter(author=request.user).order_by('created_date')
    form1 = toDoListForm()
    form2 = openCaseForm()
    
    #check if post data is for opening exixting case
    if request.method == "POST" and 'opencase' in request.POST:
    	#get patientid from user
        openCasePatientId = request.POST.get('openPatientId')
        temp = None
        #check if id exists
        try:
            temp = patient.objects.get(patientId=openCasePatientId)
        except Exception, e:
            pass
        #if exists
        if temp and temp.doc == request.user:
        	#set patienid in session
            request.session['patientId'] = openCasePatientId
        else:
        	#if doesnt exists display error message
            error_message = "This patient ID doesn't exists"
            args = {'error_message' : error_message,
            'user': request.user,
            'posts': posts,
            'form1': form1,
            'form2': form2,}
            #redirect back to diagnose with error mesaage
            return render(request, 'dashboard/dashboard.html', args)
        
        #if patientid is set redirect to diagnose
        return HttpResponseRedirect('/diagnose/')
        
    elif request.method == "POST" and 'todolist' in request.POST: #if post data is for adding a todo list
        newPost = request.POST.get('toDoPost')
        toDoList.objects.create(author=request.user, toDoPost=newPost)#create new post

    context = {'user': request.user,
    'posts': posts,
    'form1': form1,
    'form2': form2,
    }

    return render(request, 'dashboard/dashboard.html', context)

#for creating case from entered data
@login_required
def createcase(request):
    args = {}
    #get form submission data
    if request.method == 'POST':
        form = patientRegForm(request.POST)
        if form.is_valid():
            patientId = request.session['patientId']
            patient.objects.create(doc=request.user, patientId=patientId)
            patientMod = patient.objects.get(patientId=patientId) 
            Gender = request.POST.get('Gender')
            Age = request.POST.get('Age')
            Pulse = request.POST.get('Pulse')
            BloodP = request.POST.get('BloodP')
            RespirationR = request.POST.get('RespirationR')
            Height = request.POST.get('Height')
            HeightUnits = request.POST.get('HeightUnits')
            Weight = request.POST.get('Weight')
            WeightUnits = request.POST.get('WeightUnits')
            BMI = BMICalc(Height, Weight, HeightUnits, WeightUnits)
            Pallor = request.POST.get('Pallor')
            Icterus = request.POST.get('Icterus')
            Cyanosis = request.POST.get('Cyanosis')
            Clubbing = request.POST.get('Clubbing')
            Lymphadenopathy = request.POST.get('Lymphadenopathy')
            ThyroidE = request.POST.get('ThyroidE')
            PeripheralP = request.POST.get('PeripheralP')
            Csign = request.POST.get('Csign')
            Tsign = request.POST.get('Tsign')
            Petechiae = request.POST.get('Petechiae')
            Purpura = request.POST.get('Purpura')
            Acanthosis = request.POST.get('Acanthosis')
            SkinTags = request.POST.get('SkinTags')

            #create case
            case.objects.create(patientob=patientMod, Gender=Gender, Age=Age, Pulse=Pulse, BloodP=BloodP, RespirationR=RespirationR, Height=Height, HeightUnits=HeightUnits, WeightUnits=WeightUnits, Weight=Weight, BMI=BMI, Pallor=Pallor, Icterus=Icterus, Cyanosis=Cyanosis, Clubbing=Clubbing, Lymphadenopathy=Lymphadenopathy, ThyroidE=ThyroidE, PeripheralP=PeripheralP, Csign=Csign, Tsign=Tsign, Petechiae=Petechiae, Purpura=Purpura, Acanthosis=Acanthosis, SkinTags=SkinTags)

            return HttpResponseRedirect('/diagnose/')
    
    else:
    	#for generating patiendid on createcase page load
        userFullname = request.user.get_full_name()
        if len(userFullname)<1:
            userFullname = request.user.username
            userInitials = userFullname[:2].upper()
        else:
            userInitials = userFullname[0]+ userFullname[userFullname.index(' ')+1]
        newPatientId = generateId(userInitials)#genreate id from user initials 
        
        args['patientId'] = newPatientId
        request.session['patientId'] = newPatientId
    
    args.update(csrf(request))
    args['form'] = patientRegForm()
    args['user'] = request.user
    
    return render(request, 'dashboard/managecases.html', args)

#calc bmi from height weight
def BMICalc(Height, Weight, HeightUnits, WeightUnits):
    if HeightUnits == 'in':
        HeightCm = float(Height) * 2.54
    else:
        HeightCm = float(Height)
    if WeightUnits == 'lb':
        WeightKg = float(Weight) * 0.45359237
    else:
        WeightKg= float(Weight)
    bmi = (WeightKg*10000)/(HeightCm*HeightCm)
    return bmi

#generate unique patientid
def generateId(userInitials):
    newPatientId = userInitials + User.objects.make_random_password(length=8, allowed_chars='1234567890')
    try:
        if patient.objects.get(patientId=newPatientId):
            generateId(userInitials)
        else:
            return newPatientId
    except Exception, e:
        return newPatientId     

@login_required
def diagnose(request):
	#check if patientid is set in session
    try:
        patientId = request.session['patientId']
    except KeyError, e:
    	#if not then send to dashboard
        return HttpResponseRedirect('/dashboard/')
    args = {}
    args['patientId'] = patientId
    patientMod = patient.objects.get(patientId=patientId) 
    caseVar = case.objects.get(patientob=patientMod)#get the case from patientid
    args['case'] = caseVar
    return render(request, 'dashboard/diagnose.html', args)

#for testing
def diagnose1(request):
    return render(request, 'dashboard/diagnose1.html', {})

#for testing
def diagnose2(request):
    return render(request, 'dashboard/diagnose.html', {})

#ajax on symptom add
def sympadd(request):
    if request.method == 'POST':
        symp = request.POST.get('symp')
        response_data = {}
        response_data['symp'] = symp
        return HttpResponse(
            json.dumps(response_data),
            content_type='application/json'
        )

#ajax on symtom remove
def sympremove(request):
    if request.method == 'POST':
        symp = request.POST.get('symp')
        response_data = {}
        response_data['sympremove'] = symp
        return HttpResponse(
            json.dumps(response_data),
            content_type='application/json'
        )

@login_required
def aetiology(request):
    return render(request, 'dashboard/aetiology.html', {})

@login_required
def summary(request):
    return render(request, 'dashboard/summary.html', {})

def profile(request):
    return render(request, 'dashboard/profile.html', {})

@login_required
def casereport(request):
    patientId = request.session['patientId']
    args = {}
    args['patientId'] = patientId
    patientMod = patient.objects.get(patientId=patientId) 
    caseVar = case.objects.get(patientob=patientMod)
    args['case'] = caseVar
    return render(request, 'dashboard/casereport.html', args)