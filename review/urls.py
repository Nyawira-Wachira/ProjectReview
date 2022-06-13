from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.Register, name='register'),  
    path('login/',views.Login, name='login'), 
    path('logout/',views.UserLogout, name='logout'),
    path('profile/',views.UserProfile, name='profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)