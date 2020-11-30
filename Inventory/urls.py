from django.contrib import admin
from django.urls import path

from djangoapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard', views.dashboard, name='employeeDashboard'),
    path('additems', views.additems, name='additems'),
    path('dashboard/(<id>\d+)', views.product_edit, name='product_edit'),
    path('dashboard/(<id>\d+)/delete', views.product_delete, name='product_delete'),
    path('summary', views.summary, name='summary'),
    path('admin/', admin.site.urls),

    path('login', views.login_view, name="login"),
    path('logout', views.logout_view, name="logout")
]
