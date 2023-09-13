from django.contrib import admin
from django.urls import path
from Django_Services import settings
from home.views import * 
from vege.views import * 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello_world , name="index"),
    path('about/', about , name="about"),
    path('home/', home , name="home"),
    path('contact/',contact , name="contact"),
    path('recepies/', recepies, name="recepies"),
    path('recepies/delete_recepies/<id>/', delete_recepie, name="delete_recepie"),
    path('recepies/update_recepies/<id>/', update_recepie, name="updatete_recepie"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    
    urlpatterns += staticfiles_urlpatterns()
    
