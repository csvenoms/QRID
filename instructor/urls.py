from django.urls import path
from.import views
urlpatterns = [
    path('instructor', views.instructorHome, name='instructorHome'),
    path('addMaterial', views.addMaterial, name='addMaterial')
]
