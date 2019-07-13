from decimal import *
from django import forms
from django.forms import formset_factory
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import dates
from .models import Transaction, Account, Currency, Type, Category, Subcategory, Place, AccountError

# Create your views here.

#Transactions views
	
class TransactionArchiveView(dates.ArchiveIndexView):
	model = Transaction
	date_field = 'create_datetime'
	template_name = 'finance/transaction/transaction_archive.html'
	
class TransactionYearArchiveView(dates.YearArchiveView):
	model = Transaction
	date_field = 'create_datetime'
	make_object_list = True
	template_name = 'finance/transaction/transaction_archive_year.html'
	
class TransactionMonthArchiveView(dates.MonthArchiveView):
	model = Transaction
	date_field = 'create_datetime'
	month_format = '%m'
	template_name = 'finance/transaction/transaction_archive_month.html'
	allow_future = True
	
class TransactionDayArchiveView(dates.DayArchiveView):
	model = Transaction
	date_field = 'create_datetime'
	month_format = '%m'
	template_name = 'finance/transaction/transaction_archive_day.html'
	allow_future = True
	
class TransactionDetailView(generic.DetailView):
	model = Transaction
	template_name = 'finance/transaction/transaction_detail.html'
	
class TransactionCreateView(generic.CreateView):
	model = Transaction
	fields = '__all__'
	template_name = 'finance/transaction/transaction_create.html'
	
	def form_valid(self, form):
		if not form.cleaned_data.get('from_account') and not form.cleaned_data.get('on_account'):
			raise forms.ValidationError('Вкажіть хоча б один рахунок для проведення трансакції')
		return super().form_valid(form)
	
	def post(self, request, *args, **kwargs):
		amount = Decimal(request.POST.get('amount', ''))
		currency = Currency.objects.get(pk=request.POST.get('currency', ''))
		from_account = request.POST.get('from_account', '')
		on_account = request.POST.get('on_account', '')
		if from_account:
			ad = Account.objects.get(pk=from_account)
			ad.decrease(amount, currency)
			ad.save()
		if on_account:
			ai = Account.objects.get(pk=on_account)
			ai.increase(amount, currency)
			ai.save()
		return super().post(request, *args, **kwargs)
	
class TransactionEditView(generic.UpdateView):
	model = Transaction
	fields = '__all__'
	template_name = 'finance/transaction/transaction_edit.html'
	
	def form_valid(self, form):
		if not form.cleaned_data.get('from_account') and not form.cleaned_data.get('on_account'):
			raise forms.ValidationError('Вкажіть хоча б один рахунок для проведення трансакції')
		return super().form_valid(form)
	
	def post(self, request, *args, **kwargs):
		self.object = self.get_object()
		transaction = Transaction.objects.get(pk=self.object.pk)
		post_amount = Decimal(request.POST.get('amount'))
		post_currency = Currency.objects.get(pk=request.POST.get('currency'))
		
		if transaction.from_account and request.POST.get('from_account'):
			post_from_account_id = request.POST.get('from_account')
			post_from_account = Account.objects.get(pk=post_from_account_id)
			transaction_from_account = Account.objects.get(pk=transaction.from_account.id)
			
			if transaction.from_account.id == int(post_from_account_id):
				amount_diff_d = post_amount - transaction.amount
				transaction_from_account.decrease(amount_diff_d, post_currency)
				post_from_account.decrease(amount_diff_d, post_currency)
				
			else:
				transaction_from_account.increase(transaction.amount, transaction.currency)
				post_from_account.decrease(post_amount, post_currency)
				
		else:
			if transaction.from_account:
				transaction_from_account = Account.objects.get(pk=transaction.from_account.id)
				transaction_from_account.increase(transaction.amount, transaction.currency)
			
			if request.POST.get('from_account'):
				post_from_account = Account.objects.get(pk=request.POST.get('from_account'))
				post_from_account.decrease(post_amount, post_currency)
			
			
		if transaction.on_account and request.POST.get('on_account'):
			post_on_account_id = request.POST.get('on_account')
			transaction_on_account = Account.objects.get(pk=transaction.on_account.id)
			post_on_account = Account.objects.get(pk=post_on_account_id)
			
			if transaction.on_account.id == int(post_on_account_id):
				amount_diff_i = post_amount - transaction.amount
				transaction_on_account.increase(amount_diff_i, post_currency)
				post_on_account.increase(amount_diff_i, post_currency)
		
			else:
				transaction_on_account.decrease(transaction.amount, transaction.currency)
				post_on_account.increase(post_amount, post_currency)
				
		else:
			if transaction.on_account:
				transaction_on_account = Account.objects.get(pk=transaction.on_account.id)
				transaction_on_account.decrease(transaction.amount, transaction.currency)
			
			if request.POST.get('on_account'):
				post_on_account = Account.objects.get(pk=request.POST.get('on_account'))
				post_on_account.increase(post_amount, post_currency)
				
				
		if transaction.from_account:
			transaction_from_account.save()
			
		if transaction.on_account:
			transaction_on_account.save()
			
		if request.POST.get('from_account'):
			post_from_account.save()
			
		if request.POST.get('on_account'):
			post_on_account.save()
			
		return super().post(request, *args, **kwargs)
		
	
class TransactionDeleteView(generic.DeleteView):
	model = Transaction
	template_name = 'finance/transaction/transaction_confirm_delete.html'
	success_url = reverse_lazy('finance:transactions_list')
	
	def post(self, request, *args, **kwargs):
		self.object = self.get_object()
		transaction = Transaction.objects.get(pk=self.object.pk)
		if transaction.from_account:
			ai = Account.objects.get(pk=transaction.from_account.id)
			ai.increase(transaction.amount, transaction.currency)
			ai.save()
		if transaction.on_account:
			ad = Account.objects.get(pk=transaction.on_account.id)
			ad.decrease(transaction.amount, transaction.currency)
			ad.save()
		return super().post(request, *args, **kwargs)
	
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
	


class PlanCategorySpendingAddForm(forms.ModelForm):
	class Meta:
		model = Transaction
		fields = ['category', 'amount', 'currency']
	
#Planning views
def plan_spending_category_add(request):
	categories = Category.objects.all()
	PlanCategorySpendingAddFormSet = formset_factory(PlanCategorySpendingAddForm, extra = categories.count())
	if request.method == 'POST':
		formset = PlanCategorySpendingAddFormSet(request.POST)
		if formset.is_valid():
			pass
		return HttpResponseRedirect(reverse('finance:transactions_list'))
	else:
		formset = PlanCategorySpendingAddFormSet()
	
	return render(request, 'finance/planning/plan_category_spending_add.html', {'formset': formset})
    
def plan_spending_category_add(edit):
    pass





















	