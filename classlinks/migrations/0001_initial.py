# Generated by Django 3.1.2 on 2020-10-15 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0003_remove_user_lastpayment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.batch')),
            ],
        ),
    ]
