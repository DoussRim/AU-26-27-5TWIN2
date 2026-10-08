
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    #path('login/',auth_views.LoginView.as_view(template_name='Person/login.html')),
    path('login/',auth_views.LoginView.as_view(),name="log"),
    # path('login/',auth_views.LoginView.as_view(
        # template_name='Person/login.html')),

    path('logout/',auth_views.LogoutView.as_view(),name="out"),
    path('SignUp/',views.SignUp,name="Register")
    ]

