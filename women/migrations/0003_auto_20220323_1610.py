# Generated by Django 3.2.9 on 2022-03-23 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0002_auto_20220322_1623'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='women',
            options={'ordering': ['time_created', 'title'], 'verbose_name': 'Famous Women', 'verbose_name_plural': 'Famous Women'},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(db_index=True, max_length=100, verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='women',
            name='content',
            field=models.TextField(blank=True, verbose_name='Autobiography'),
        ),
        migrations.AlterField(
            model_name='women',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Name Surname'),
        ),
    ]
