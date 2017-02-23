from django.shortcuts import render, redirect
from .models import Course

def index(request):
	context = {
		'courses': Course.objects.all()
	}
	return render(request, 'courses/index.html',context)

def create(request):
	Course.objects.create(name = request.POST['name'], description = request.POST['description'])

	return redirect('/')


def delete(request, id):
	course = Course.objects.get(pk=id)
	context = {
		'second': course
	}

	return render(request, 'courses/delete.html', context)

def destroy(request):
	if 'yes' in request.POST:
		id = request.POST['course_id']
		Course.objects.filter(id = id).delete()
		return redirect('/')
	elif 'no' in request.POST:
		return redirect('/')





