from django.shortcuts import render
from courses.models import Course
from lessons.models import Lesson
from tests.models import Test

def in_user_group(user):
    return user.is_authenticated and user.groups.filter(name = 'User').exists()

# Create your views here.
def Index(request, *args, **kwargs):
    courses = Course.objects.all()
    return render(request, "index.html", {'courses': courses})

def Users(request, *args, **kwargs):
    return render(request, "users.html", {})

def Courses(request, *args, **kwargs):
    courses = Course.objects.all()
    return render(request, "courses.html", {'courses': courses})

def OneCourse(request, id):
    course = Course.objects.get(id = id)
    lessons = Lesson.objects.filter(course_id = id)
    tests = Test.objects.filter(course_id = id)
    return render(request, "course.html", {'course': course, 'lessons': lessons, 'tests': tests})

def OneLesson(request, course_id, id):
    lesson = Lesson.objects.get(course_id = course_id, id = id)
    return render(request, "lesson.html", {'lesson': lesson})

def Tests(request, course_id):
    tests = Test.objects.filter(course_id = course_id)
    return render(request, "tests.html", {'tests': tests, 'course_id': course_id})

def TestResults(request, course_id):
    tests = Test.objects.filter(course_id = course_id)
    total = 0
    for test in tests:
        total += test.points
    return render(request, "test-results.html", {'total': total, 'course_id': course_id})

def About(request, *args, **kwargs):
    return render(request, "about.html", {})

def Contacts(request, *args, **kwargs):
    return render(request, "contacts.html", {})

def AdminIndex(request, *args, **kwargs):
    return render(request, "admin/index.html", {})
