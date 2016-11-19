from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth                 
from django.template.context_processors import csrf 
from form import patientRegistrationForm

def casereport(request):
    return render(request, 'dashboard/casereport.html', {})

def dashboard(request):
    context = {'user': request.user}
    return render(request, 'dashboard/dashboard.html', context)

def managecases(request):
    if request.method == 'POST':
        form = patientRegistrationForm(request.POST)     # create form object
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/createcase/complete')
    args = {}
    args.update(csrf(request))
    args['form'] = patientRegistrationForm()
    print args
    return render(request, 'dashboard/managecases.html', args)

def case_creation_complete(request):
    return render_to_response('dashboard/diagnose.html')

def diagnose(request):
    return render(request, 'dashboard/diagnose.html', {})

def aetiology(request):
    return render(request, 'dashboard/aetiology.html', {})

def summary(request):
    return render(request, 'dashboard/summary.html', {})