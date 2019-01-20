from django.shortcuts import render, redirect, HttpResponse
from datetime import datetime
from ..app_one.models import *
from .models import Work
from django.contrib import messages



def main(request):
    context = {
        'user': User.objects.all,
        'one' : User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'handy_app/index.html')
    

def add(request):

    return render(request,'handy_app/add.html')

def processadd(request):
    if request.method=='POST':
        errors = Work.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request,value)
            return redirect('/')
        else:
            add_new_user = User.objects.get(id=request.session['user_id'])
            job = Work.objects.create(title = request.POST['title'],destination=request.POST['destination'], description=request.POST['description'],user_created = add_new_user)
            # job.user_created.add(add_new_user)
    return redirect('/main')



def show(request):
    return render(request, 'handy_app/show.html')

def edit(request):
    return render(request, 'handy_app/edit.html')