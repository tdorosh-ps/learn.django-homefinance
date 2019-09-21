from django.urls import path

from .import views

app_name = 'finance'

urlpatterns = [
	
	#path('home/', name='home'),
	
	#Accounting urls
	#path('accounting/', name='accounting'),
	
		#Transactions urls
	path('accounting/transactions/', views.TransactionArchiveView.as_view(), name='transactions_list'),
	path('accounting/transactions/<int:year>/', views.TransactionYearArchiveView.as_view(), name='archive_year'),
	path('accounting/transactions/<int:year>/<int:month>/', views.TransactionMonthArchiveView.as_view(), name='archive_month'),
	path('accounting/transactions/<int:year>/<int:month>/<int:day>/', views.TransactionDayArchiveView.as_view(), name='archive_day'),
	path('accounting/transactions/create/', views.TransactionCreateView.as_view(), name='transaction_create'),
	path('accounting/transactions/id/<int:pk>/', views.TransactionDetailView.as_view(), name='transaction_detail'),
	path('accounting/transactions/id/<int:pk>/edit/', views.TransactionEditView.as_view(), name='transaction_edit'),
	path('accounting/transactions/id/<int:pk>/delete/', views.TransactionDeleteView.as_view(), name='transaction_delete'),
	
		#Account urls
	path('accounting/accounts/', views.AccountsListView.as_view(), name='accounts_list'),
	path('accounting/accounts/<int:pk>/', views.AccountDetailView.as_view(), name='account_detail'),
	path('accounting/accounts/create/', views.AccountCreateView.as_view(), name='account_create'),
	path('accounting/accounts/<int:pk>/edit/', views.AccountEditView.as_view(), name='account_edit'),
	path('accounting/accounts/<int:pk>/delete/', views.AccountDeleteView.as_view(), name='account_delete'),
	
		#Currencies urls
	path('accounting/currencies/', views.CurrenciesListView.as_view(), name='currencies_list'),
	path('accounting/currencies/create/', views.CurrencyCreateView.as_view(), name='currency_create'),
	path('accounting/currencies/<int:pk>/edit/', views.CurrencyEditView.as_view(), name='currency_edit'),
	path('accounting/currencies/<int:pk>/delete/', views.CurrencyDeleteView.as_view(), name='currency_delete'),
	
		#Types urls
	path('accounting/types/', views.TypesListView.as_view(), name='types_list'),
	path('accounting/types/create/', views.TypeCreateView.as_view(), name='type_create'),
	path('accounting/types/<int:pk>/edit/', views.TypeEditView.as_view(), name='type_edit'),
	path('accounting/types/<int:pk>/delete/', views.TypeDeleteView.as_view(), name='type_delete'),
	
		#Category urls
	path('accounting/categories/', views.CategoriesListView.as_view(), name='categories_list'),
	path('accounting/categories/create/', views.CategoryCreateView.as_view(), name='category_create'),
	path('accounting/categories/<int:pk>/edit/', views.CategoryEditView.as_view(), name='category_edit'),
	path('accounting/categories/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category_delete'),
	
		#Subcategories urls
	path('accounting/subcategories/', views.SubcategoriesListView.as_view(), name='subcategories_list'),
	path('accounting/subcategories/create/', views.SubcategoryCreateView.as_view(), name='subcategory_create'),
	path('accounting/subcategories/<int:pk>/edit/', views.SubcategoryEditView.as_view(), name='subcategory_edit'),
	path('accounting/subcategories/<int:pk>/delete/', views.SubcategoryDeleteView.as_view(), name='subcategory_delete'),
	
		#Places urls
	path('accounting/places/', views.PlacesListView.as_view(), name='places_list'),
	path('accounting/places/create/', views.PlaceCreateView.as_view(), name='place_create'),
	path('accounting/places/<int:pk>/edit/', views.PlaceEditView.as_view(), name='place_edit'),
	path('accounting/places/<int:pk>/delete/', views.PlaceDeleteView.as_view(), name='place_delete'),
	
	#Statistics urls
	#path('statistics', name='statistics'),
	
	#Planning urls
	#path('planning/spending/category/add', views.plan_spending_category_add, name='plan_spending_category_add'),
    #path('planning/spending/category/edit'), views.plan_spending_category_edit, name='plan_spending_category_add'),
]
