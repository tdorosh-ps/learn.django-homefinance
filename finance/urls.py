from django.urls import path

from .import views

app_name = 'finance'

urlpatterns = [
	
	path('home/', name='home'),
	
	#Accounting urls
	path('accounting/', name='accounting'),
	
		#Transactions urls
	path('accounting/transactions/', views.TransactionsListView.as_view(), name='transactions_list'),
	path('accounting/transactions/<int:pk>/', views.TransactionDetailView.as_view(), name='transaction_detail'),
	path('accounting/transactions/create/', views.TransactionCreateView.as_view(), name='transaction_create'),
	path('accounting/transactions/<int:pk>/edit/', views.TransactionEditView.as_view(), name='transaction_edit'),
	path('accounting/transactions/<int:pk>/delete/', views.TransactionDeleteView.as_view(), name='transaction_delete'),
	
		#Account urls
	path('accounting/accounts/', views.AccountsListView.as_view(), name='accounts_list'),
	path('accounting/accounts/<int:pk>/', views.AccountDetailView.as_view(), name='account_detail'),
	path('accounting/accounts/create/', views.AccountCreateView.as_view(), name='account_create'),
	path('accounting/accounts/<int:pk>/edit/', views.AccountEditView.as_view(), name='account_edit'),
	path('accounting/accounts/<int:pk>/delete/', views.AccountDeleteView.as_view(), name='account_delete'),
	
		#
]