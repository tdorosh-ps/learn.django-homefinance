from django.db import models
from django.utils import timezone
# Create your models here.
class Transaction(models.Model):
	amount = models.DecimalField('Сума', max_digits=11, decimal_places=2, default='00000,00')
	currencies = models.ForeignKey('Currency', verbose_name='Валюта', on_delete=models.PROTECT, default=lambda: Currency.objects.get(is_default=True)
	types = models.ForeignKey('Type', verbose_name='Тип', on_delete=models.PROTECT)
	categories = models.ForeignKey('Category', verbose_name='Категорія', on_delete=models.PROTECT, limit_choices_to={})
	subcategories = models.ForeignKey('Subcategory', verbose_name='Підкатегорія', on_delete=models.PROTECT, limit_choices_to={})
	from_account = models.ForeignKey('Account', verbose_name='З рахунку', on_delete=models.PROTECT)
	on_account = models.ForeignKey('Account', verbose_name='На рахунок', on_delete=models.PROTECT)
	create_datetime = models.DateTimeField('Дата здійснення', default=timezone.now)
	notes = models.TextField('Додаткові відомості')
	
	class Meta(object):
		ordering = ['-date_time']
		verbose_name = 'Трансакція'
		verbose_name_plural = 'Трансакції'
		
	def __str__(self):
		return '{}, {} {}, {}'.format(self.notes, self.amount, self.currency, self.create_datetime)
		
		
class Account(models.Model):
	title = model.CharField('Назва', max_length=255)
	amount = model.DecimalField('Залишок', max_digits=11, decimal_places=2, default='00000,00')
	notes = models.TextField('Додаткові відомості')
	create_datetime = models.DateTimeField('Дата створення', default=timezone.now)
	is_default = model.BooleanField('За замовчуванням')
	
	class Meta(object):
		ordering = ['amount']
		verbose_name = 'Рахунок'
		verbose_name_plural = 'Рахунки'
		
	def __str__(self):
		return '{}, {}'.format(self.title, self.amount)
		
class Currency(models.Model):
	name = model.CharField('Назва', max_length=5)
	full_name = model.CharField('Повна назва', max_length=100)
	is_default = model.BooleanField('За замовчуванням')
	
	class Meta(object):
		verbose_name = 'Валюта'
		verbose_name_plural = 'Валюти'
		
	def __str__(self):
		return '{}, {}'.format(self.full_name, self.name)
		
class Type(model.Models):
	name = model.CharField('Назва', max_length=100)
	categories = models.ForeignKey('Category', verbose_name='Категорії', on_delete=models.PROTECT)
	
	class Meta(object):
		verbose_name = 'Тип'
		verbose_name_plural = 'Типи'
		
	def __str__(self):
		return '{}'.format(self.name)
	
class Category(model.Models):
	name = model.CharField('Назва', max_length=100)
	subcategories = models.ForeignKey('Subсategory', verbose_name='Підкатегорії', on_delete=models.PROTECT)
	
	class Meta(object):
		verbose_name = 'Категорія'
		verbose_name_plural = 'Категорії'
		
	def __str__(self):
		return '{}'.format(self.name)
	
	
class Subcategory(model.Models):
	name = model.CharField('Назва', max_length=100)
	
	class Meta(object):
		verbose_name = 'Підкатегорія'
		verbose_name_plural = 'Підкатегорії'
		
	def __str__(self):
		return '{}'.format(self.name)
	
	
	
	