# Generated by Django 3.0.14 on 2022-11-24 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction_types', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction_type',
            name='type',
            field=models.CharField(choices=[('debit', 'Debit'), ('ticket', 'Ticket'), ('financing', 'Financing'), ('credit', 'Credit'), ('loan', 'Loan Income'), ('sale', 'Sale'), ('express tranfer', 'Transfer Ted'), ('standard tranfer', 'Tranfer Pod'), ('rent', 'Rent')], max_length=17, unique=True),
        ),
    ]
