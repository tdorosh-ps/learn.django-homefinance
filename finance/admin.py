from django.contrib import admin
from .models import Transaction, Account, Currency, Type, Category, Subcategory, Place
# Register your models here.

admin.site.register(Transaction)
admin.site.register(Account)
admin.site.register(Currency)
admin.site.register(Type)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Place)
