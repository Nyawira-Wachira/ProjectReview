from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
     path('home/',views.home, name='home'),
    path('',views.Register, name='register'),  
    path('login/',views.Login, name='login'), 
    path('logout/',views.UserLogout, name='logout'),
    path('profile/',views.UserProfile, name='profile'),
    path('update/',views.ProfileUpdate, name='update'),
    path('project/',views.Project, name='project'),
    path('search/', views.search_results, name='search_results'),
    path('<uuid:project_id>/',views.ProjectDetails, name='projectdetails'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)