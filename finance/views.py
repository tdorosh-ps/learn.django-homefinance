from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import Transaction, Account, Currency, Type, Category, Subcategory, Place

# Create your views here.
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