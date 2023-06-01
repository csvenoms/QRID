from django.urls import path
from . import views
from collageRegistrar import views as crv
urlpatterns = [
    path('',views.dashboard),
    path('reg',views.reg, name="home"),
    path('login',views.login, name="login"),
    path('login',views.login, name="login"),
    path('UserSaveAnnouncements',views.GetSavedAnnouncements.as_view(), name="UserSaveAnnouncements"),
    path('getUserSaveAnnouncements/<str:pk>',views.SavedAnnouncementApi.as_view(), name="getUserAnnouncements"),
    path('deleteSaved/<str:pk>/<str:pk2>/', views.DeleteUserSavedMessages.as_view(),name="deleteSaved"),
    path('getUserData/<str:pk>/', views.GetUserInfo.as_view(), name="getUserData"),
    path('profile/', views.UserProfileUpdateView.as_view(), name='user_profile_update'),
]
