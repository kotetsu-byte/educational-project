from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Lesson
# Create your views here.

@login_required(login_url='/page-admin/login')
def AdminLessonIndex(request, course_id):
    lessons = Lesson.objects.filter(course_id = course_id).order_by('id')
    return render(request, "admin/lessons/index.html", {'lessons': lessons, 'course_id': course_id})

@login_required(login_url='/page-admin/login')
def AdminLessonDetails(request, course_id, id):
    lesson = Lesson.objects.get(course_id = course_id, id = id)
    return render(request, "admin/lessons/details.html", {'lesson': lesson})

@csrf_exempt
@login_required(login_url='/page-admin/login')
def AdminLessonCreate(request, course_id):
    if request.method == "POST":
        lesson = Lesson.objects.create(
            title = request.POST.get('title'),
            info = request.POST.get('info'),
            course_id = course_id
        )
        lesson.save()
    return render(request, "admin/lessons/create.html", {'message': 'Created Successfully', 'course_id': course_id})

@csrf_exempt
@login_required(login_url='/page-admin/login')
def AdminLessonEdit(request, course_id, id):
    lesson = Lesson.objects.get(course_id = course_id, id = id)
    if request.method == "POST":
        lesson.title = request.POST.get('title')
        lesson.info = request.POST.get('info')
        lesson.save()
    return render(request, "admin/lessons/edit.html", {'lesson': lesson})

@csrf_exempt
@login_required(login_url='/page-admin/login')
def AdminLessonDelete(request):
    Lesson.objects.get(id = request.POST.get('id')).delete()
    return HttpResponse('ok')