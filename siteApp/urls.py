from django.contrib import admin
from django.urls import path
from . import views

app_name = "siteAppUrls"


urlpatterns = [
    path('', views.indexPage, name="indexPage"),
    path('about', views.aboutPage, name="aboutPage"),
    path('blog_single', views.blog_singlePage, name="blog_singlePage"),
    path('blog', views.blogPage, name="blogPage"),
    path('contact', views.contactPage, name="contactPage"),
    path('services', views.servicesPage, name="servicesPage"),
    path('work', views.workPage, name="workPage"),
    path('login', views.loginPage, name="loginPage"),
    path('signup', views.signupPage, name="signupPage"),
    path('forget', views.forgetPage, name="forgetPage"),



]
