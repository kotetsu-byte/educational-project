from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import Course


# Create your views here.
@login_required(login_url = '/page-admin/login')
def AdminCourseIndex(request, *args, **kwargs):
    courses = Course.objects.all().order_by('id')
    context = {
        'courses': courses
    }
    return render(request, "admin/courses/index.html", context)


@login_required(login_url = '/page-admin/login')
def AdminCourseDetails(request, id):
    course = Course.objects.get(id = id)
    context = {
        'course': course
    }
    return render(request, "admin/courses/details.html", context)

@csrf_exempt
@login_required(login_url = '/page-admin/login')
def AdminCourseCreate(request, *args, **kwargs):
    if request.method == "POST":
        course = Course.objects.create(
            name = request.POST.get('name'),
            description = request.POST.get('description'),
        )
        course.save()
    return render(request, "admin/courses/create.html", {'message': 'Created Successfully!'})

@csrf_exempt
@login_required(login_url = '/page-admin/login')
def AdminCourseEdit(request, id):
    course = Course.objects.get(id = id)
    if request.method == "POST":
        course.name = request.POST.get('name')
        course.description = request.POST.get('description')
        course.save()
    return render(request, "admin/courses/edit.html", {'course': course})

@csrf_exempt
@login_required(login_url = '/page-admin/login')
def AdminCourseDelete(request):
    Course.objects.get(id = request.POST.get('id')).delete()
    return HttpResponse('ok')