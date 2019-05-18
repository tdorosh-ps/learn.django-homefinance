from django.shortcuts import render
from django.views import generic
from .models import Transaction, Account, Currency, Type, Category, Subcategory, Place

# Create your views here.
class TransactionsListView(generic.ListView):
	model = Transaction
	template_name = 'finance/transactions_list.html'