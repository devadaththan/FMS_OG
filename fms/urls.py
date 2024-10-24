from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.home,name="home_page"),
    path("about/",views.about,name='about_page'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('admin/login/', auth_views.LoginView.as_view(), name='admin_login'),
    path('user/',views.staff_view,name='user_dashbord'),
    path("principal/",views.princi, name="principal_dashbord"),
    path("superintendent/",views.superintendent_view , name="superintendent_dashbord"),
    path('new_files/',views.new_files_created,name='newfile_page'),
    path('dashboard_redirect/', views.dashboard_redirect, name='dashboard_redirect'),
    path('pemding_files/',views.pending_file,name='pendingfile_page'),

]