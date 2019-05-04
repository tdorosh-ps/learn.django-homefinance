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
	