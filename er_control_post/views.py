from django.shortcuts import render,get_object_or_404,redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.contrib import messages
from django.db.models import Q
from .models import post
from .forms import PostForm


def form(request):
	form = PostForm(request.POST or None)
	context = {
		'views_title': 'create',
		'btn': 'Create',
		'form': form
	}
	messages.success(request, 'Be careful about job details')
	return render(request,"form.html",context)


# Create View
def post_create(request):
	form = PostForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		messages.success(request,'Successfuly Created')
		return HttpResponseRedirect(instance.get_url())
	context = {
	'views_title':'create',
	'btn':'Create',
	'form':form
	}
	messages.error(request, 'Error, check your data well')
	return render(request, "form.html", context)


def post_detail(request,id):
	instance = get_object_or_404(post,id=id)
	context = {
	'views_title':'detail',
	'instance':instance
	}
	return render(request,"detail.html",context)


def post_list(request):
	queryset = post.objects.filter(user=request.user.id).order_by('-puplish')
	q = request.GET.get('q')
	if q:
		queryset = queryset.filter(
			Q(job_title__icontains=q)|
			Q(company__icontains=q))
	context = {
	'views_title':'list',
	'queryset':queryset
	}
	return render(request,"list.html",context)


# def post_update(request,id):
# 	instance = get_object_or_404(post,id=id)
# 	form = PostForm(request.POST or None,instance=instance)
# 	if form.is_valid():
# 		instance = form.save(commit=False)
# 		instance.save()
# 		messages.success(request,'item saved')
# 		return HttpResponseRedirect(instance.get_url())
# 	context = {
# 	'views_title':'update',
# 	'instance':instance,
# 	'btn':'Edit',
# 	'form':form
# 	}
# 	return render(request,"form.html",context)


def post_delete(request,id):
	instance = get_object_or_404(post,id=id)
	instance.delete()
	messages.success(request,'Successfuly deleted')
	return redirect('list')