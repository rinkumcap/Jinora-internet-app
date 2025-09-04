
from django.urls import path
from . import views

urlpatterns = [

    # Login/Dashboard url  =========================================
    path('', views.admin_login_view, name='admin_login'), 
    path('logout', views.admin_logout_view, name='admin_logout'),
    path('dashboard/', views.dashboard_view, name='dashboard_view'), 
    path('app/', views.app_list, name='app_list'), 
    path('app/add/', views.app_add, name='app_add'), 
    path("app/edit/<int:app_id>/", views.app_edit, name="app_edit"),
    path("app/delete/<int:app_id>/", views.app_delete, name="app_delete"),
  
          
]
