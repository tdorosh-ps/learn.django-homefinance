from django.db import models
from django.utils import timezone
# Create your models here.
class Transaction(models.Model):
	amount = models.DecimalField('Сума', max_digits=11, decimal_places=2, default='00000,00')
	currency = models.ForeignKey('Currency', verbose_name='Валюта', on_delete=models.PROTECT, default=lambda: Currency.objects.get(is_default=True)
	type = models.ForeignKey('Type', verbose_name='Тип', on_delete=models.PROTECT)
	category = models.ForeignKey('Category', verbose_name='Категорія', on_delete=models.PROTECT, limit_choices_to={})
	subcategory = models.ForeignKey('Subcategory', verbose_name='Підкатегорія', on_delete=models.PROTECT, limit_choices_to={})
	from_account = models.ForeignKey('Account', verbose_name='З рахунку', on_delete=models.PROTECT)
	on_account = models.ForeignKey('Account', verbose_name='На рахунок', on_delete=models.PROTECT)
	create_datetime = models.DateTimeField(default=timezone.now)
	notes = models.TextField()
	
	class Meta(object):
		ordering = ['-date_time']
		verbose_name = 'Трансакція'
		verbose_name_plural = 'Трансакції'
		
	def __str__(self):
		return '{}, {} {}, {}'.format(self.notes, self.amount, self.currency, self.create_datetime)
		
		
class Account(models.Model):
	title = model.CharField('Назва', max_length=255)
	amount = model.DecimalField('Залишок', max_digits=11, decimal_places=2, default='00000,00')
	notes = models.TextField()
	create_datetime = models.DateTimeField(default=timezone.now)
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
		ordering = ['name']
		verbose_name = 'Валюта'
		verbose_name_plural = 'Валюти'
		
	def __str__(self):
		return '{}, {}'.format(self.full_name, self.name)
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	