"""
URL configuration for uranus project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from pages.views import Index
from pages.views import Courses
from pages.views import OneCourse
from pages.views import OneLesson
from pages.views import Tests
from pages.views import TestResults
from pages.views import About
from pages.views import Contacts
from pages.views import AdminIndex

from courses.views import AdminCourseIndex
from courses.views import AdminCourseDetails
from courses.views import AdminCourseCreate
from courses.views import AdminCourseEdit
from courses.views import AdminCourseDelete

from lessons.views import AdminLessonIndex
from lessons.views import AdminLessonDetails
from lessons.views import AdminLessonCreate
from lessons.views import AdminLessonEdit
from lessons.views import AdminLessonDelete

from tests.views import AdminTestIndex
from tests.views import AdminTestDetails
from tests.views import AdminTestCreate
from tests.views import AdminTestEdit
from tests.views import AdminTestDelete

from login.views import AdminRegister
from login.views import AdminLogin
from login.views import AdminLogout

from login.views import AdminUserIndex
from login.views import AdminUserDetails
from login.views import AdminUserDelete

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', Index),
    path('courses/', Courses),
    path('course/<int:id>', OneCourse),
    path('lesson/<int:course_id>/<int:id>', OneLesson),
    path('tests/<int:course_id>', Tests),
    path('test-results/<int:course_id>', TestResults),
    path('about/', About),
    path('contacts/', Contacts),
    path('page-admin/', AdminIndex),
    #admin-course
    path('page-admin/courses/', AdminCourseIndex),
    path('page-admin/courses/<int:id>/', AdminCourseDetails),
    path('page-admin/courses/create', AdminCourseCreate, name="course_create"),
    path('page-admin/courses/edit/<int:id>', AdminCourseEdit, name="course_edit"),
    path('page-admin/courses/delete/', AdminCourseDelete, name="course_delete"),
    #admin-lesson
    path('page-admin/lessons/<int:course_id>/', AdminLessonIndex),
    path('page-admin/lessons/<int:course_id>/<int:id>/', AdminLessonDetails),
    path('page-admin/lessons/create/<int:course_id>', AdminLessonCreate, name="lesson_create"),
    path('page-admin/lessons/edit/<int:course_id>/<int:id>/', AdminLessonEdit, name="lesson_edit"),
    path('page_admin/lessons/delete/', AdminLessonDelete, name="lesson_delete"),
    #admin-test
    path('page-admin/tests/<int:course_id>/', AdminTestIndex),
    path('page-admin/tests/<int:course_id>/<int:id>/', AdminTestDetails),
    path('page-admin/tests/create/<int:course_id>', AdminTestCreate, name="test_create"),
    path('page-admin/tests/edit/<int:course_id>/<int:id>/', AdminTestEdit, name="test_edit"),
    path('page_admin/tests/delete/', AdminTestDelete, name="test_delete"),
    #admin-user
    path('page-admin/users', AdminUserIndex),
    path('page-admin/users/<int:id>', AdminUserDetails),
    path('page-admin/users/delete', AdminUserDelete, name="user_delete"),

    #auth
    path('page-admin/register/', AdminRegister, name="admin-register"),
    path('page-admin/login/', AdminLogin, name="admin-login"),
    path('page-admin/logout/', AdminLogout, name="admin-logout")
]