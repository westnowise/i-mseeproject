from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import login.views


urlpatterns = [
    path('',login.views.index, name='index'),
    path('adminhome',login.views.adminhome, name='adminhome'),
    path('admin/', admin.site.urls),
    path('sort/',include('sort.urls')),
    path('accounts/', include('login.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
