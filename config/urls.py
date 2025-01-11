"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import app.views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app.views.home, name ="home"),
    path('login/', app.views.login_PAGE, name='Login'),
    path('logout/', app.views.logout_PAGE, name='logout'),
    path('register/', app.views.register_PAGE, name='register'),
    path('events/', app.views.view_events, name='view_events'),
    path('events/', app.views.event_list, name='event_list'),
    path('events/<int:event_id>/edit/', app.views.edit_event, name='edit_event'),
    path('events/<int:event_id>/purchase/', app.views.purchase_ticket, name='purchase_ticket'),
    path('user_tickets/', app.views.user_tickets, name='user_tickets'),
    path('events/add/', app.views.add_event, name='add_event'),
    path('events/remove/<int:event_id>/', app.views.remove_event, name='remove_event'),
]
