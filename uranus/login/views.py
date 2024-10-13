from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# Create your views here.
@csrf_exempt
def AdminLogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return HttpResponse('ok')
    return render(request, "admin/login.html", {})

@csrf_exempt
def AdminRegister(request):
    if request.method == "POST":
        user = User.objects.create_user(
            first_name = request.POST.get('firstName'),
            last_name = request.POST.get('lastName'),
            email = request.POST.get('email'),
            username = request.POST.get('username'),
            password = request.POST.get('password')
        )
        user.save()
        return HttpResponse('ok')
    return render(request, "admin/register.html", {})

@csrf_exempt
def AdminLogout(request):
    if request.method == "POST":
        active = request.POST.get('active')
        if active == 'yes':
            logout(request)
            return HttpResponse('ok')
    return render(request, "admin/header.html", {})

@csrf_exempt
def AdminUserIndex(request):
    users = User.objects.all().order_by('id')
    return render(request, "admin/users/index.html", {'users': users})

@csrf_exempt
def AdminUserDetails(request, id):
    user = User.objects.get(id = id)
    return render(request, "admin/users/details.html", {'user': user})

@csrf_exempt
def AdminUserDelete(request):
    User.objects.get(id = request.POST.get('id')).delete()
    return HttpResponse('ok')