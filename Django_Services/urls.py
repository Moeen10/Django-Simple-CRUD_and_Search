from django.contrib import admin
from django.urls import path
from Django_Services import settings
from home.views import * 
from vege.views import * 
from shed.views import *
from incentory_expense_remaining.views import *
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
    path('login/', loginPage, name="login"),
    path('register/', registration, name="register"),
    path('logout/', logout_page, name="logout"),
    path('shed_registration/', shed_registration, name = "shed_registration"),
    path('inventory_add/', inventory_add, name = "inventory_add"),
    path('inventory_list/', inventory_list, name = "inventory_list"),
    path('remaining_inventory_list/', remaining_inventory_list, name = "remaining_inventory_list"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    
    urlpatterns += staticfiles_urlpatterns()
    
