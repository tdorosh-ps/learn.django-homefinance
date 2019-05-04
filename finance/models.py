from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator
# Create your models here.
class Transaction(models.Model):
	amount = models.DecimalField('Сума', max_digits=11, decimal_places=2, default=0, validators=[MinValueValidator(0)])
	currencies = models.ForeignKey('Currency', verbose_name='Валюта', on_delete=models.PROTECT)
	types = models.ForeignKey('Type', verbose_name='Тип', on_delete=models.PROTECT)
	categories = models.ForeignKey('Category', verbose_name='Категорія', on_delete=models.PROTECT, limit_choices_to={}, blank=True)
	subcategories = models.ForeignKey('Subcategory', verbose_name='Підкатегорія', on_delete=models.PROTECT, limit_choices_to={}, blank=True, null=True)
	from_account = models.ForeignKey('Account', related_name='from_account_set', verbose_name='З рахунку', on_delete=models.PROTECT, blank=True, null=True)
	on_account = models.ForeignKey('Account', related_name='on_account_set', verbose_name='На рахунок', on_delete=models.PROTECT, blank=True, null=True)
	create_datetime = models.DateTimeField('Дата здійснення', default=timezone.now)
	place = models.ForeignKey('Place', verbose_name='Місце', on_delete=models.PROTECT, blank=True, default='')
	notes = models.TextField('Додаткові відомості', blank=True)
	
	class Meta(object):
		ordering = ['-create_datetime']
		verbose_name = 'Трансакція'
		verbose_name_plural = 'Трансакції'
		
	def __str__(self):
		return '{}, {} {}, {}'.format(self.notes, self.amount, self.currencies, self.create_datetime)
		
		
class Account(models.Model):
	title = models.CharField('Назва', max_length=255)
	amount = models.DecimalField('Залишок', max_digits=11, decimal_places=2, default=0, validators=[MinValueValidator(0)])
	notes = models.TextField('Додаткові відомості', blank=True)
	create_datetime = models.DateTimeField('Дата створення', default=timezone.now)
	is_default = models.BooleanField('За замовчуванням')
	
	class Meta(object):
		ordering = ['amount']
		verbose_name = 'Рахунок'
		verbose_name_plural = 'Рахунки'
		
	def __str__(self):
		return '{}, {}'.format(self.title, self.amount)
		
	def increase(self, sum):
		self.amount += sum
			
	def decrease(self, sum):
		if self.amount >= sum:
			self.amount -= sum
		else:
			return 'На рахунку недостатньо коштів. Поповніть спочатку рахунок'
		
		
class Currency(models.Model):
	name = models.CharField('Назва', max_length=5)
	full_name = models.CharField('Повна назва', max_length=100, blank=True)
	is_default = models.BooleanField('За замовчуванням')
	
	class Meta(object):
		verbose_name = 'Валюта'
		verbose_name_plural = 'Валюти'
		
	def __str__(self):
		return '{}'.format(self.name)
		
class Type(models.Model):
	name = models.CharField('Назва', max_length=100)
	
	class Meta(object):
		verbose_name = 'Тип'
		verbose_name_plural = 'Типи'
		
	def __str__(self):
		return '{}'.format(self.name)
	
class Category(models.Model):
	name = models.CharField('Назва', max_length=100)
	type = models.ForeignKey('Type', verbose_name='Тип', on_delete=models.PROTECT)
	
	class Meta(object):
		verbose_name = 'Категорія'
		verbose_name_plural = 'Категорії'
		
	def __str__(self):
		return '{}'.format(self.name)
	
	
class Subcategory(models.Model):
	name = models.CharField('Назва', max_length=100)
	category = models.ForeignKey('Category', verbose_name='Категорія', on_delete=models.PROTECT)
	
	class Meta(object):
		verbose_name = 'Підкатегорія'
		verbose_name_plural = 'Підкатегорії'
		
	def __str__(self):
		return '{}'.format(self.name)
		
class Place(models.Model):
	name = models.CharField('Назва', max_length=100)
	
	class Meta(object):
		verbose_name = 'Місце'
		verbose_name_plural = 'Місця'
		
	def __str__(self):
		return '{}'.format(self.name)
	
	
	
	