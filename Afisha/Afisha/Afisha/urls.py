from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from movie_app import urls as movie_app_urls

def home(request):
    return HttpResponse('Welcome to the Afisha Movie API!')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('api/v1/', include('movie_app.urls')),

]
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(movie_app_urls)),

]

from django.http import HttpResponse
from django.urls import path, include

def home(request):
    return HttpResponse("Welcome to the Afisha API!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('movie_app.urls')),
    path('', home),
]

urlpatterns = [
    path('api/v1/users/', include('your_app.urls')),
]

