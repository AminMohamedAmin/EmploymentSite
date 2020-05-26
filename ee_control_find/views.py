from django.shortcuts import render, render, HttpResponse, HttpResponseRedirect, redirect, get_object_or_404
from ee_control_upload import models as file
from django.contrib import messages
from django.db.models import Q
from ee_control_upload.models import file as lld
from ee_control_find.models import like as likes
from ee_control_find.models import dislike as dislikes
from ee_control_find.models import love as loves
# Create your views here.


def index(request, username):
    query = file.file.objects.all()
    q = request.GET.get('q')
    if q:
        query = query.filter(
            Q(job__icontains=q) |
            Q(username__icontains=q)
        )
        lov = loves.objects.filter(employer=username)
        lovv = lov.values_list('employee', flat=True).distinct()
        messages.warning(request, 'check CVs well to find a good employee.', extra_tags='warning')
        return render(request,'employer.html',{'query':query, 'q':q, 'uu':username, 'lovv':lovv})
    else:
        lov = loves.objects.filter(employer=username)
        lovv = lov.values_list('employee', flat=True).distinct()
        messages.error(request, 'no CVs found.', extra_tags='error')
        return render(request,'employer.html',{'uu':username, 'lovv':lovv})

def like(request,username):
    d = lld.objects.get(username=username)
    li = likes()
    li.employer = request.user.username
    li.employee = d.username
    li.cv = d.file
    li.job = d.job
    if d.username != request.user.username:
        old1 = dislikes.objects.filter(employer=request.user.username, employee=username)
        old2 = loves.objects.filter(employer=request.user.username, employee=username)
        old1.delete()
        old2.delete()
        if likes.objects.filter(employer=request.user.username, employee=username).exists()==False :
            li.save()
        return HttpResponse('Thanks, your Evaluation will help the Employee. Close this page and continue')
    else:
        return render(request, 'employer.html', {'uu': username})


def dislike(request,username):
    d = lld.objects.get(username=username)
    di = dislikes()
    di.employer = request.user.username
    di.employee = d.username
    di.cv = d.file
    di.job = d.job
    if d.username != request.user.username:
        old1 = likes.objects.filter(employer=request.user.username, employee=username)
        old2 = loves.objects.filter(employer=request.user.username, employee=username)
        old1.delete()
        old2.delete()
        if dislikes.objects.filter(employer=request.user.username, employee=username).exists()==False :
            di.save()
        return HttpResponse('Thanks, your Evaluation will help the Employee. Close this page and continue')
    else:
        return render(request, 'employer.html', {'uu': username})


def love(request,username):
    d = lld.objects.get(username=username)
    lo = loves()
    lo.employer = request.user.username
    lo.employee = d.username
    lo.cv = d.file
    lo.job = d.job
    if d.username != request.user.username:
        old1 = dislikes.objects.filter(employer=request.user.username, employee=username)
        old2 = likes.objects.filter(employer=request.user.username, employee=username)
        old1.delete()
        old2.delete()
        if loves.objects.filter(employer=request.user.username, employee=username).exists()==False :
            lo.save()
        return HttpResponse('Thanks, your Evaluation will help the Employee. Close this page and continue')
    else:
        return render(request, 'employer.html', {'uu': username})


def loved(request):
    loved = loves.objects.filter(employer=request.user.username).values('employee','cv', 'job').distinct()
    return render(request, 'loved.html', {'loved':loved})
