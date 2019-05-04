# Generated by Django 2.2 on 2019-05-04 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Назва')),
            ],
            options={
                'verbose_name': 'Місце',
                'verbose_name_plural': 'Місця',
            },
        ),
        migrations.AlterField(
            model_name='account',
            name='notes',
            field=models.TextField(blank=True, verbose_name='Додаткові відомості'),
        ),
        migrations.AlterField(
            model_name='currency',
            name='full_name',
            field=models.CharField(blank=True, max_length=100, verbose_name='Повна назва'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='categories',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='finance.Category', verbose_name='Категорія'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='from_account',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='from_account_set', to='finance.Account', verbose_name='З рахунку'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='notes',
            field=models.TextField(blank=True, verbose_name='Додаткові відомості'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='on_account',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='on_account_set', to='finance.Account', verbose_name='На рахунок'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='subcategories',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='finance.Subcategory', verbose_name='Підкатегорія'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='place',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.PROTECT, to='finance.Place', verbose_name='Місце'),
        ),
    ]
