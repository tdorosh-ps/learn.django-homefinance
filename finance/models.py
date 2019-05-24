from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.core.validators import MinValueValidator

#Exception Class

class AccountError(Exception):
	def __init__(self, text):
		self.txt = text


# Create your models here.

class Transaction(models.Model):
	amount = models.DecimalField('Сума', max_digits=11, decimal_places=2, default=0, validators=[MinValueValidator(0.01)])
	currency = models.ForeignKey('Currency', verbose_name='Валюта', on_delete=models.PROTECT)
	trans_type = models.ForeignKey('Type', verbose_name='Тип', on_delete=models.PROTECT, blank=True, null=True)
	category = models.ForeignKey('Category', verbose_name='Категорія', on_delete=models.PROTECT, blank=True, null=True)
	subcategory = models.ForeignKey('Subcategory', verbose_name='Підкатегорія', on_delete=models.PROTECT, blank=True, null=True)
	from_account = models.ForeignKey('Account', related_name='from_account', verbose_name='З рахунку', on_delete=models.PROTECT, blank=True, null=True)
	on_account = models.ForeignKey('Account', related_name='on_account', verbose_name='На рахунок', on_delete=models.PROTECT, blank=True, null=True)
	create_datetime = models.DateTimeField('Дата здійснення', default=timezone.now)
	place = models.ForeignKey('Place', verbose_name='Місце', on_delete=models.PROTECT, blank=True, null=True)
	notes = models.TextField('Додаткові відомості', blank=True)
	
	def get_absolute_url(self):
		return reverse('finance:transaction_detail', kwargs={'pk': self.pk})
	
	class Meta(object):
		ordering = ['-create_datetime']
		verbose_name = 'Трансакція'
		verbose_name_plural = 'Трансакції'
		
	def __str__(self):
		return '{}, {} {}, {}'.format(self.notes, self.amount, self.currency, self.create_datetime)
		
		
class Account(models.Model):
	title = models.CharField('Назва', max_length=100)
	amount = models.DecimalField('Залишок', max_digits=11, decimal_places=2, default=0, validators=[MinValueValidator(0)], blank=False, null=False)
	currency = models.ForeignKey('Currency', verbose_name='Валюта рахунку', on_delete=models.PROTECT)
	notes = models.TextField('Додаткові відомості', blank=True)
	create_datetime = models.DateTimeField('Дата створення', default=timezone.now)
	
	def get_absolute_url(self):
		return reverse('finance:account_detail', kwargs={'pk': self.pk})
	
	class Meta(object):
		ordering = ['amount']
		verbose_name = 'Рахунок'
		verbose_name_plural = 'Рахунки'
		
	def __str__(self):
		return '{}, {}'.format(self.title, self.amount)
		
	def increase(self, sum, currency):
		if self.currency == currency:
			self.amount += sum
		else:
			raise AccountError('Валюта рахунку має співвпадати з валютою трансакції')
			
	def decrease(self, sum, currency):
		if self.amount < sum:
			raise AccountError('На рахунку недостатньо коштів. Поповніть спочатку рахунок')
		elif self.currency != currency:
			raise AccountError('Валюта рахунку має співвпадати з валютою трансакції')
		else:
			self.amount -= sum
		
		
class Currency(models.Model):
	name = models.CharField('Назва', max_length=5)
	full_name = models.CharField('Повна назва', max_length=50, blank=True)
	
	class Meta(object):
		verbose_name = 'Валюта'
		verbose_name_plural = 'Валюти'
		
	def __str__(self):
		return '{}'.format(self.name)
		
class Type(models.Model):
	name = models.CharField('Назва', max_length=20)
	
	class Meta(object):
		verbose_name = 'Тип'
		verbose_name_plural = 'Типи'
		
	def __str__(self):
		return '{}'.format(self.name)
	
class Category(models.Model):
	name = models.CharField('Назва', max_length=20)
	type = models.ForeignKey('Type', verbose_name='Тип', on_delete=models.PROTECT)
	
	class Meta(object):
		verbose_name = 'Категорія'
		verbose_name_plural = 'Категорії'
		
	def __str__(self):
		return '{}'.format(self.name)
	
	
class Subcategory(models.Model):
	name = models.CharField('Назва', max_length=20)
	category = models.ForeignKey('Category', verbose_name='Категорія', on_delete=models.PROTECT)
	
	class Meta(object):
		verbose_name = 'Підкатегорія'
		verbose_name_plural = 'Підкатегорії'
		
	def __str__(self):
		return '{}'.format(self.name)
		
class Place(models.Model):
	name = models.CharField('Назва', max_length=50)
	
	class Meta(object):
		verbose_name = 'Місце'
		verbose_name_plural = 'Місця'
		
	def __str__(self):
		return '{}'.format(self.name)
	
	
	
	