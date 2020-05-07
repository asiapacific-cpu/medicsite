from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from medic.views import *
from . import views

urlpatterns = [
    path('', home, name="dashboard"),
    path('about-us/', about_us, name="about-us"),
    path('contact-us/', contactform, name="contact-us"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
