"""qr_studId URL Configuration

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
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from . import views
from dashboard import views as dsview
@csrf_exempt
def my_endpoint(request):
    if request.method == 'GET':
        data = {'message': 'Hello from my custom endpoint!'}
        return JsonResponse(data)
    else:
        return HttpResponse(status=405) 


urlpatterns = [
    path("admin/",  admin.site.urls),
    path("", include("dashboard.urls")),
    path("api_logout", views.Logout.as_view()),
    path("gateguard/", include("gateguard.urls")),
    path('instructor/', include('instructor.urls')),  
    path('registrar/', include('collageRegistrar.urls')), 
    path('api-token-auth/', views.CustomAuthToken.as_view()),
    path('api_login',views.MyView.as_view()),
    path('api/my_endpoint/', my_endpoint, name='my_endpoint'),
    path('message/', include("chat.urls")),
    path('logout',dsview.logout, name="logout"),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)