from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("authentication.urls")),
    path("", include("web.urls")),
    path('__debug__/', include('debug_toolbar.urls')),
]
