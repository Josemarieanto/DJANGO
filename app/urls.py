from django.urls import path
from . import views

urlpatterns = [
    # path("admin/", admin.site.urls),
    path("home",views.home),
    path("about" , views.about),
    path("programs" , views.programs),
    path("admissions" , views.admissions),
    path("contact" , views.contact),
]