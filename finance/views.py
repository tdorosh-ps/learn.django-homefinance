from decimal import *

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import Transaction, Account, Currency, Type, Category, Subcategory, Place, AccountError

# Create your views here.

#Transactions views
class TransactionsListView(generic.ListView):
	model = Transaction
	template_name = 'finance/transaction/transactions_list.html'
	
class TransactionDetailView(generic.DetailView):
	model = Transaction
	template_name = 'finance/transaction/transaction_detail.html'
	
class TransactionCreateView(generic.CreateView):
	model = Transaction
	fields = '__all__'
	template_name = 'finance/transaction/transaction_create.html'
	
	def post(self, request, *args, **kwargs):
		amount = Decimal(request.POST.get('amount', ''))
		currency = Currency.objects.get(pk=request.POST.get('currency', ''))
		from_account = request.POST.get('from_account', '')
		on_account = request.POST.get('on_account', '')
		if from_account:
			ad = Account.objects.get(pk=from_account)
			try:
				ad.decrease(amount, currency)
			except AccountError as ae:
				pass
			else:
				ad.save()
		if on_account:
			ai = Account.objects.get(pk=on_account)
			try:
				ai.increase(amount, currency)
			except AccountError as ae:
				pass
			else:
				ai.save()
		return super().post(request, *args, **kwargs)
	
class TransactionEditView(generic.UpdateView):
	model = Transaction
	fields = '__all__'
	template_name = 'finance/transaction/transaction_edit.html'
	
class TransactionDeleteView(generic.DeleteView):
	model = Transaction
	template_name = 'finance/transaction/transaction_confirm_delete.html'
	success_url = reverse_lazy('finance:transactions_list')
	
#Accounts views	
	
class AccountsListView(generic.ListView):
	model = Account
	template_name = 'finance/account/accounts_list.html'
	
class AccountDetailView(generic.DetailView):
	model = Account
	template_name = 'finance/account/account_detail.html'
	
class AccountCreateView(generic.CreateView):
	model = Account
	fields = '__all__'
	template_name = 'finance/account/account_create.html'
	
class AccountEditView(generic.UpdateView):
	model = Account
	fields = '__all__'
	template_name = 'finance/account/account_edit.html'
	
class AccountDeleteView(generic.DeleteView):
	model = Account
	template_name = 'finance/account/account_confirm_delete.html'
	success_url = reverse_lazy('finance:accounts_list')
	
#Currencies views

class CurrenciesListView(generic.ListView):
	model = Currency
	template_name = 'finance/currency/currencies_list.html'
	
class CurrencyCreateView(generic.CreateView):
	model = Currency
	fields = '__all__'
	template_name = 'finance/currency/currency_create.html'
	success_url = reverse_lazy('finance:currencies_list')
	
class CurrencyEditView(generic.UpdateView):
	model = Currency
	fields = '__all__'
	template_name = 'finance/currency/currency_edit.html'
	success_url = reverse_lazy('finance:currencies_list')
	
class CurrencyDeleteView(generic.DeleteView):
	model = Currency
	template_name = 'finance/currency/currency_confirm_delete.html'
	success_url = reverse_lazy('finance:currencies_list')
	
#Types views

class TypesListView(generic.ListView):
	model = Type
	template_name = 'finance/type/types_list.html'
	
class TypeCreateView(generic.CreateView):
	model = Type
	fields = '__all__'
	template_name = 'finance/type/type_create.html'
	success_url = reverse_lazy('finance:types_list')
	
class TypeEditView(generic.UpdateView):
	model = Type
	fields = '__all__'
	template_name = 'finance/type/type_edit.html'
	success_url = reverse_lazy('finance:types_list')
	
class TypeDeleteView(generic.DeleteView):
	model = Type
	template_name = 'finance/type/type_confirm_delete.html'
	success_url = reverse_lazy('finance:types_list')	
	
#Categories views

class CategoriesListView(generic.ListView):
	model = Category
	template_name = 'finance/category/categories_list.html'
	
class CategoryCreateView(generic.CreateView):
	model = Category
	fields = '__all__'
	template_name = 'finance/category/category_create.html'
	success_url = reverse_lazy('finance:categories_list')
	
class CategoryEditView(generic.UpdateView):
	model = Category
	fields = '__all__'
	template_name = 'finance/category/category_edit.html'
	success_url = reverse_lazy('finance:categories_list')
	
class CategoryDeleteView(generic.DeleteView):
	model = Category
	template_name = 'finance/category/category_confirm_delete.html'
	success_url = reverse_lazy('finance:categories_list')
	
#Subcategories views

class SubcategoriesListView(generic.ListView):
	model = Subcategory
	template_name = 'finance/subcategory/subcategories_list.html'
	
class SubcategoryCreateView(generic.CreateView):
	model = Subcategory
	fields = '__all__'
	template_name = 'finance/subcategory/subcategory_create.html'
	success_url = reverse_lazy('finance:subcategories_list')
	
class SubcategoryEditView(generic.UpdateView):
	model = Subcategory
	fields = '__all__'
	template_name = 'finance/subcategory/subcategory_edit.html'
	success_url = reverse_lazy('finance:subcategories_list')
	
class SubcategoryDeleteView(generic.DeleteView):
	model = Subcategory
	template_name = 'finance/subcategory/subcategory_confirm_delete.html'
	success_url = reverse_lazy('finance:subcategories_list')
	
#Places views

class PlacesListView(generic.ListView):
	model = Place
	template_name = 'finance/place/places_list.html'
	
class PlaceCreateView(generic.CreateView):
	model = Place
	fields = '__all__'
	template_name = 'finance/place/place_create.html'
	success_url = reverse_lazy('finance:places_list')
	
class PlaceEditView(generic.UpdateView):
	model = Place
	fields = '__all__'
	template_name = 'finance/place/place_edit.html'
	success_url = reverse_lazy('finance:places_list')
	
class PlaceDeleteView(generic.DeleteView):
	model = Place
	template_name = 'finance/place/place_confirm_delete.html'
	success_url = reverse_lazy('finance:places_list')
	