from django.contrib import admin
from django.urls import path
from Django_Services import settings
from home.views import * 
from vege.views import * 
from shed.views import *
from cow.views import *
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

    # Authentication Apis

    path('login/', loginPage, name="login"),
    path('register/', registration, name="register"),
    path('logout/', logout_page, name="logout"),

#    Cow Profile related apis

    # path('allCow/', allCow, name = "allCow"),
    path('reqiestForAllCowProfile/', CowProfile.as_view(), name = "reqiestForAllCowProfile"),


#   Shed related api
    
    path('api/sheds/', list_sheds, name='shed-list'),
    path('shed_registration/', shed_registration, name = "shed_registration"),

#    Inventory related apis

    path('inventory_add/', inventory_add, name = "inventory_add"),
    path('allAddInventory/', allAddInventory, name = "allAddInventory"),
    path('inventory_list/', inventory_list, name = "inventory_list"),
    path('remaining_inventory_list/', remaining_inventory_list, name = "remaining_inventory_list"),

#    Test er jonno use kora hoise hudai ignore it 
    path('asche/', FormDataView.as_view(), name = "remaining_inventory_list"),

#    Cow profile registration dorkari apis
    path('cow_registration_web/', cow_registration, name = "cow_registration"),
    path('alldesease/', MasterDeseaseList.as_view(), name = "all_desease"),
    path('allvaccine/', MasterVaccineList.as_view(), name = "allvaccine"),
    path('allmedicine/', MasterMedicineList.as_view(), name = "allmedicine"),
    path('postCow/', CowRegistrationView.as_view(), name = "postCow"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    
    urlpatterns += staticfiles_urlpatterns()
    
