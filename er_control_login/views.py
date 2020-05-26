from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.

def in_loginn(request):
    return render(request, 'loginn.html', {})


def up_sighnn(request):
    try:
        if User.objects.filter(email=request.POST['eml']) and not User.objects.filter(username=request.POST['u_name']):
            messages.error(request, 'Email exist, try Login', extra_tags='error')
            return render(request, 'loginn.html', {})
        else:
            user = User.objects.create_user(request.POST['u_name'], request.POST['eml'], request.POST['pass'])
            user.first_name = request.POST['f_name']
            user.last_name = request.POST['l_name']
            user.save()
            messages.success(request, 'Successfuly Signed, Login now', extra_tags='success')
            return render(request, 'loginn.html', {})
    except:
        if User.objects.filter(email=request.POST['eml']) and User.objects.filter(username=request.POST['u_name']).exists() == True:
            messages.error(request, 'User exist, try Login', extra_tags='error')
        else:
            messages.error(request, 'User exist, try another', extra_tags='error')
        return render(request, 'loginn.html', {})


def employee_loginn(request):
    u = request.POST['u_Name']
    p= request.POST['pAss']
    result=authenticate(username=u,password=p)
    if result is not None:
        login(request,result)
        messages.info(request, 'Search with your job title in your CV', extra_tags='info')
        return render(request, 'search.html', {'u':u})
    else:
        messages.error(request, 'User not exist or Password is wrong, Sighnup first', extra_tags='error')
        return render(request, 'loginn.html', {})


    # if file.objects.filter(username=request.POST['userName']).exists() == True:
    #     user = request.POST['userName']
    #     data = file.objects.get(username=user)
    #     v = viwers.objects.filter(employee=user)
    #     vv = v.values_list('employer', flat=True).distinct()
    #     messages.info(request, 'Be careful about your job data', extra_tags='info')
    #     return render(request, 'employee2.html', {'form':form, 'uu':user, 'd':data, 'v':v, 'vv':vv})
    # else:
    #     u=request.POST['userName']
    #     p= request.POST['passWord']
    #     result=authenticate(username=u,password=p)
    #     if result is not None:
    #         login(request,result)
    #         messages.info(request, 'Be careful about your job data', extra_tags='info')
    #         return render(request, 'emloyee.html', {'form':form, 'uu':u})
    #     else:
    #         messages.error(request, 'User not exist, Sighnup first', extra_tags='error')
    #         return render(request, 'loginn.html', {})



def employer_loginn(request):
    u=request.POST['U_name']
    p= request.POST['Pass']
    result=authenticate(username=u,password=p)
    if result is not None:
        login(request,result)
        messages.info(request, 'Hello Employer', extra_tags='info')
        messages.info(request, 'Create a clear post please ', extra_tags='info')
        return render(request, 'post.html', {'uu': u})
    else:
        messages.error(request, 'User not exist or Password is wrong, Sighnup first', extra_tags='error')
        return render(request, 'loginn.html', {})


def employer_logoutt(request):
    logout(request)
    return HttpResponseRedirect('../inlogg')


def backhomee(request):
    return HttpResponseRedirect('/')