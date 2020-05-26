from django.shortcuts import render, HttpResponseRedirect, HttpResponse, redirect
from . import models
from . import forms
from django.http import FileResponse
from django.contrib.auth.models import User
from django.contrib import messages
from ee_control_find import models as savecv
# Create your views here.
from ee_control_find.models import SavedCV as viwers
import os
from ee_control_find.models import like as likes
from ee_control_find.models import dislike as dislikes
from ee_control_find.models import love as loves


def save_file(request, username):
    userr = models.file()
    us = User.objects.get(username=username)
    form = forms.file_form(request.POST, request.FILES)
    if form.is_valid():
        userr.username = request.POST['UserName']
        userr.job = request.POST['JobTitle']
        userr.level = request.POST['Level']
        userr.file = form.cleaned_data['file']
        userr.save()
        v = viwers.objects.filter(employee=userr.username)
        vv = v.values_list('employer', flat=True).distinct()
        lik = likes.objects.filter(employee=userr.username)
        likk = lik.values_list('employer', flat=True).distinct()
        dlik = dislikes.objects.filter(employee=userr.username)
        dlikk = dlik.values_list('employer', flat=True).distinct()
        lov = loves.objects.filter(employee=userr.username)
        lovv = lov.values_list('employer', flat=True).distinct()
        messages.success(request, 'Successfuly Saved, wait an opportunity soon', extra_tags='success')
        return render(request, 'employee3.html', {'form': form, 'dd':userr, 'uu':userr.username, 'v':v, 'vv':vv, 'likk':likk, 'dlikk':dlikk, 'lovv':lovv,})
    messages.warning(request, 'Failed Saved, check your data well', extra_tags='warning')
    return render(request, 'emloyee.html', {'form': form, 'uu':us})


def read_file(request,username):
    d = models.file.objects.get(username=username)
    cv = savecv.SavedCV()
    cv.employer = request.user.username
    cv.employee = d.username
    cv.cv = d.file
    cv.job = d.job
    if d.username != request.user.username:
        cv.save()
        file = open(d.file.path, 'rb')
        response = HttpResponse(file, content_type='application/pdf')
        return response
        # return FileResponse(open(d.file.path, 'rb'))
    else:
        file = open(d.file.path, 'rb')
        response = HttpResponse(file, content_type='application/pdf')
        return response
        # return FileResponse(open(d.file.path, 'rb'))

def update_file(request, username):
    form = forms.file_form(request.POST, request.FILES)
    use = request.POST['UserName']
    uuss = models.file.objects.get(username=username)
    if form.is_valid():
        JobTitle = request.POST['JobTitle']
        Level = request.POST['Level']
        File = form.cleaned_data['file']

        new = models.file(username=username)
        new.job = JobTitle
        new.level = Level
        new.file = File
        os.remove(uuss.file.path)
        new.save()
        v = viwers.objects.filter(employee=use)
        vv = v.values_list('employer', flat=True).distinct()
        lik = likes.objects.filter(employee=use)
        likk = lik.values_list('employer', flat=True).distinct()
        dlik = dislikes.objects.filter(employee=use)
        dlikk = dlik.values_list('employer', flat=True).distinct()
        lov = loves.objects.filter(employee=use)
        lovv = lov.values_list('employer', flat=True).distinct()
        messages.success(request, 'Successfuly updated', extra_tags='success')
        return render(request, 'employee4.html',{'uu':use, 'n':new, 'form':form, 'v':v, 'vv':vv, 'likk':likk, 'dlikk':dlikk, 'lovv':lovv,})
    v = viwers.objects.filter(employee=use)
    vv = v.values_list('employer', flat=True).distinct()
    lik = likes.objects.filter(employee=use)
    likk = lik.values_list('employer', flat=True).distinct()
    dlik = dislikes.objects.filter(employee=use)
    dlikk = dlik.values_list('employer', flat=True).distinct()
    lov = loves.objects.filter(employee=use)
    lovv = lov.values_list('employer', flat=True).distinct()
    messages.warning(request, 'form is not valid, check you data well', extra_tags='warning')
    return render(request, 'employee3.html', {'form': form, 'dd':uuss, 'uu':use, 'v':v, 'vv':vv, 'likk':likk, 'dlikk':dlikk, 'lovv':lovv,})


def delete_file(request,username):
    old=models.file(username=username)
    old2 = savecv.SavedCV.objects.filter(employee=username)
    d = models.file.objects.get(username=username)
    os.remove(d.file.path)
    old.delete()
    old2.delete()
    messages.success(request, 'Successfuly job data deleted, find data still existing to add another job data at anytime', extra_tags='success')
    return HttpResponseRedirect('../../../ee_control_login/inlog/')
