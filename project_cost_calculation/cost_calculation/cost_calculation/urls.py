"""cost_calculation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from cost_management.views import my_expense,add_expense,edit_expense,delete_expense

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/', my_expense, name='cost-list'),
    path('add/', add_expense, name='add_expense'),
    path('edit/<expense_id>/', edit_expense, name='edit_expense'),
    path('delete/<expense_id>/', delete_expense, name='delete-expense'),
]
