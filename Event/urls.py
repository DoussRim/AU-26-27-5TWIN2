
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import Affiche
urlpatterns = [
    
    path('home/',views.home,name="h"),
    path('list/',views.listEvent,name="list"),
    path('list_Gen/',Affiche.as_view(),name="list_Gen"),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
