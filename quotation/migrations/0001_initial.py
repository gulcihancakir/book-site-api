# Generated by Django 3.2.6 on 2021-09-13 08:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('book', '0001_initial'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuotationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quotation', models.CharField(max_length=500)),
                ('quotation_page', models.IntegerField(blank=True, null=True)),
                ('published_date', models.DateTimeField(auto_now=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='book.bookmodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='account.usermodel')),
            ],
        ),
        migrations.CreateModel(
            name='RequotationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quotation', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='quotation.quotationmodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='account.usermodel')),
            ],
        ),
        migrations.AddConstraint(
            model_name='quotationmodel',
            constraint=models.UniqueConstraint(fields=('book', 'quotation_page', 'quotation'), name='same_book_quotation_constraints'),
        ),
    ]
