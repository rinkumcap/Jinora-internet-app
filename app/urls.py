

from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    # Login/Dashboard url  =========================================
    path('', views.home_view, name='home'),
    path("download/<int:app_id>/", views.download_app_file, name="download_app_file"),

    path("update-download-count/<int:app_id>/",views.update_download_count, name="update_download_count"),

 
]

  

