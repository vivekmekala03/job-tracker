from django.urls import path
from . import views

urlpatterns = [
    path('',              views.dashboard,   name='dashboard'),
    path('register',      views.register_view, name='register'),
    path('login',         views.login_view,  name='login'),
    path('logout',        views.logout_view, name='logout'),
    path('add',           views.add_job,     name='add_job'),
    path('edit/<int:pk>', views.edit_job,    name='edit_job'),
    path('delete/<int:pk>', views.delete_job, name='delete_job'),
]