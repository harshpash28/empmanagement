from django.contrib import admin
from django.urls import path
from empapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('index',views.index),
    path('allemp',views.allemp),
    path('removeemp/<eid>',views.remove),
    path('addnemp',views.addnemp),
    path('editemp/<eid>',views.editemp),
    path('search',views.search),
    path('sort/<sv>',views.sort),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
