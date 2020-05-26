from django.shortcuts import render,get_object_or_404,redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.contrib import messages
from django.db.models import Q
from er_control_post.models import post
from er_control_post.forms import PostForm
# Create your views here.


def posts_list(request):
    qset = post.objects.all().order_by('-puplish')
    qq = request.GET.get('qq')
    if qq:
        qset = qset.filter(
            Q(job_title__icontains=qq)|
            Q(company__icontains=qq))
    paginator = Paginator(qset, 10)
    page_var = 'page'
    page = request.GET.get(page_var)
    try:
        qquerysett = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        qquerysett = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        qquerysett = paginator.page(paginator.num_pages)
    context = {
    'views_title':'list',
    'qset':qset,
    'query': qquerysett,
    'page_var': page_var,
    }
    messages.success(request, 'Check jobs and contact the companies.', extra_tags='success')
    return render(request,"search.html",context)


def posts_detail(request, id):
    instance = get_object_or_404(post, id=id)
    context = {
        'instance': instance
    }
    return render(request, 'details.html',context)


def home(request):
    return render(request, 'search.html', {})