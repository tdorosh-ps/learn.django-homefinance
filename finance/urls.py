from django.urls import path

from .import views

app_name = 'finance'

urlpatterns = [
	
	#path('home/', name='home'),
	
	#Accounting urls
	#path('accounting/', name='accounting'),
	
		#Transactions urls
	path('accounting/transactions/', views.TransactionsListView.as_view(), name='transactions_list'),
	
	path('accounting/transactions/<int:pk>/', views.TransactionDetailView.as_view(), name='transaction_detail'),
	path('accounting/transactions/create/', views.TransactionCreateView.as_view(), name='transaction_create'),
	path('accounting/transactions/<int:pk>/edit/', views.TransactionEditView.as_view(), name='transaction_edit'),
	path('accounting/transactions/<int:pk>/delete/', views.TransactionDeleteView.as_view(), name='transaction_delete'),
	
	
]