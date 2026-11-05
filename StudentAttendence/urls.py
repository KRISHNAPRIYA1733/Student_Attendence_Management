"""
URL configuration for StudentAttendence project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from Attendence import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/',views.StudentView.as_view()),
    path('attendence/',views.AttendenceView.as_view()),
    path('student/<int:pk>/',views.StudentDetailView.as_view()),
    path('attendence/<int:pk>/',views.AttndenceDetailView.as_view()),
    path('studentAttendence/<int:pk>/',views.StudentAttendanceView.as_view()),
    path('dateAttendence/<str:date>/',views.DateAttendenceView.as_view()),
    path('Percentage/<int:pk>/',views.AttendencePercentageView.as_view())
]
