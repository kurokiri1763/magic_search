from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from search.views import magic_search
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/', include('search.urls')),
    # path('accounts/', include('accounts.urls')),
    path('add/', include('add.urls')),
    path('edit/', include('edit.urls')),
    path('/',include('search.urls')),
]

if settings.DEBUG:  # DEBUGモードのときのみ
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
