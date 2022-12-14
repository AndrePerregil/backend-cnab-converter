# Generated by Django 3.0.14 on 2022-11-23 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('debit', 'Debit'), ('ticket', 'Ticket'), ('financing', 'Financing'), ('credit', 'Credit'), ('loan', 'Loan Income'), ('sale', 'Sale'), ('express tranfer', 'Transfer Ted'), ('standard tranfer', 'Tranfer Pod'), ('rent', 'Rent')], max_length=17)),
                ('nature', models.CharField(choices=[('income', 'Income'), ('expense', 'Expense')], max_length=7)),
            ],
        ),
    ]
