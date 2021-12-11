
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def projects(request):
    return HttpResponse('Here are our products')

def project(request, pk):
    return HttpResponse('Here is Single product'+ ' ' +str(pk))

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('home/', getHomePage),
    path('projects/', projects, name='projects'),
    path('project/<str:pk>/', project, name='project'),

    # path('profiles/', admin.site.urls),
]
