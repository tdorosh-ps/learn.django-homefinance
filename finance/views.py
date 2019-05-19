from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import Transaction, Account, Currency, Type, Category, Subcategory, Place

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
	