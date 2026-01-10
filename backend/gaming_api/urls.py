from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", lambda r: HttpResponse("Backend running successfully")),
    path('api/', include('gaming_app.urls')),
]
