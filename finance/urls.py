from django.urls import path

from .import views

app_name = 'finance'

urlpatterns = [
	path('', views.transactions_list, name='home'),
]