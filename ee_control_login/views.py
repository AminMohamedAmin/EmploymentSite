from django.shortcuts import render, HttpResponseRedirect
from ee_control_upload.models import file
from ee_control_upload.forms import file_form
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.
from ee_control_find.models import SavedCV as viwers
from ee_control_find.models import like as likes
from ee_control_find.models import dislike as dislikes
from ee_control_find.models import love as loves

def in_log(request):
    return render(request, 'login.html', {})


def up_sighn(request):
    try:
        if User.objects.filter(email=request.POST['email']) and not User.objects.filter(username=request.POST['username']):
            messages.error(request, 'Email exist, try Login', extra_tags='error')
            return render(request, 'login.html', {})
        else:
            user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.save()
            messages.success(request, 'Successfuly Signed, Login now', extra_tags='success')
            return render(request, 'login.html',{})
    except:
        if User.objects.filter(email=request.POST['email']) and User.objects.filter(username=request.POST['username']).exists() == True:
            messages.error(request, 'User exist, try Login', extra_tags='error')
        else:
            messages.error(request, 'User exist, try another', extra_tags='error')
        return render(request, 'login.html',{})


def employee_login(request):
    form = file_form(request.POST, request.FILES)
    u=request.POST['userName']
    p= request.POST['passWord']
    result=authenticate(username=u,password=p)
    if result is not None:
        login(request,result)
        if file.objects.filter(username=request.POST['userName']).exists() == True:
            user = request.POST['userName']
            data = file.objects.get(username=user)
            v = viwers.objects.filter(employee=user)
            vv = v.values_list('employer', flat=True).distinct()
            lik = likes.objects.filter(employee=user)
            likk = lik.values_list('employer', flat=True).distinct()
            dlik = dislikes.objects.filter(employee=user)
            dlikk = dlik.values_list('employer', flat=True).distinct()
            lov = loves.objects.filter(employee=user)
            lovv = lov.values_list('employer', flat=True).distinct()
            # vv= vv - int(3)
            messages.info(request, 'Be careful about your job data', extra_tags='info')
            return render(request, 'employee2.html', {'form':form, 'uu':user, 'd':data, 'v':v, 'vv':vv, 'likk':likk, 'dlikk':dlikk, 'lovv':lovv,})
        messages.info(request, 'Be careful about your job data', extra_tags='info')
        return render(request, 'emloyee.html', {'form':form, 'uu':u})
    else:
        messages.error(request, 'User not exist or Password is wrong, Sighnup first', extra_tags='error')
        return render(request, 'login.html', {})



def employer_login(request):
    u=request.POST['USername']
    p= request.POST['PAssword']
    result=authenticate(username=u,password=p)
    if result is not None:
        login(request,result)
        lov = loves.objects.filter(employer=u)
        lovv = lov.values_list('employee', flat=True).distinct()
        messages.info(request, 'Be careful about your job title', extra_tags='info')
        return render(request, 'employer.html', {'uu': u, 'lovv':lovv, 'lov':lov})
    else:
        messages.error(request, 'User not exist or Password is wrong, Sighnup first', extra_tags='error')
        return render(request, 'login.html', {})


def employee_logout(request):
    logout(request)
    return HttpResponseRedirect('../inlog/')

def backhome(request):
    return HttpResponseRedirect('/')