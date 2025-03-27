from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.main),
    path('account/', include('account.urls')),
    path('habits/', include('habits.urls')),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
