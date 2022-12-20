"""firstweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from firstweb import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homePage, name="home"),
    path('about-us/', views.aboutus, name="about"),
    path('education/', views.education, name="education"),
    path('portfolios/', views.portfolio, name="portfolios"),
    path('contact/', views.contact, name="contact"),
    path('contactenquriy/', views.contactenquriy, name="contactenquriy"),
    path('userForm/', views.userForm, name="userForm"),
    path('submitform/', views.submitform, name="submitform"),
    path('course/<courseid>', views.courseDetails),
    path('evenodd/', views.evenodd, name="evenodd"),
    path('newsdetails/<slug>', views.newsDetail, name="newsdetails"),
]
