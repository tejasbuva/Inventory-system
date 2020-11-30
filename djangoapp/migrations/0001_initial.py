# Generated by Django 2.2.7 on 2020-01-19 15:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tagging.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_Name', models.CharField(blank=True, max_length=30)),
                ('Status', models.CharField(choices=[('Available', 'Available'), ('Unavailable', 'Unavailable')], max_length=30)),
                ('Serial_No', models.CharField(max_length=30, unique=True)),
                ('Issues', models.CharField(blank=True, max_length=280)),
                ('Cost_in_Euro', models.PositiveIntegerField(blank=True, default=0)),
                ('Description', models.TextField(blank=True, max_length=280)),
                ('Purchase_Date', models.DateField(blank=True, null=True)),
                ('Date_Modified', models.DateField(auto_now_add=True)),
                ('Tags', tagging.fields.TagField(blank=True, max_length=255)),
                ('Product_Group', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
                ('User_Name', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
