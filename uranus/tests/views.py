from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Test
# Create your views here.

@login_required(login_url='/page-admin/login')
def AdminTestIndex(request, course_id):
    tests = Test.objects.filter(course_id = course_id).order_by('id')
    return render(request, "admin/tests/index.html", {'tests': tests, 'course_id': course_id})

@login_required(login_url='/page-admin/login')
def AdminTestDetails(request, course_id, id):
    test = Test.objects.get(course_id = course_id, id = id)
    return render(request, "admin/tests/details.html", {'test': test})

@csrf_exempt
@login_required(login_url='/page-admin/login')
def AdminTestCreate(request, course_id):
    if request.method == "POST":
        test = Test.objects.create(
            question = request.POST.get('question'),
            answer1 = request.POST.get('answer1'),
            answer2 = request.POST.get('asnwer2'),
            answer3 = request.POST.get('answer3'),
            answer4 = request.POST.get('answer4'),
            correct_answer = request.POST.get('correct_answer'),
            points = request.POST.get('points'),
            course_id = course_id
        )
        test.save()
    return render(request, "admin/tests/create.html", {'message': 'Created Successfully', 'course_id': course_id})

@csrf_exempt
@login_required(login_url='/page-admin/login')
def AdminTestEdit(request, course_id, id):
    test = Test.objects.get(course_id = course_id, id = id)
    if request.method == "POST":
        test.question = request.POST.get('question')
        test.answer1 = request.POST.get('answer1')
        test.answer2 = request.POST.get('answer2')
        test.answer3 = request.POST.get('answer3')
        test.answer4 = request.POST.get('answer4')
        test.correct_answer = request.POST.get('correct_answer')
        test.points = request.POST.get('points')
        test.save()
    return render(request, "admin/tests/edit.html", {'test': test})
        
@csrf_exempt
@login_required(login_url='/page-admin/login')
def AdminTestDelete(request):
    Test.objects.get(id = request.POST.get('id')).delete()
    return HttpResponse('ok')