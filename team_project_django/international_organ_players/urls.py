from django.urls import path

from . import views
# from .views import AttendanceListView

app_name = 'cmgt_internal'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='register'),
]