from django.shortcuts import render
#from .models import Transaction

# Create your views here.
def transactions_list(request):
	transactions = Transaction.objects.all()
	return render(request, 'finance/transactions_list.html', {'transactions': transactions})