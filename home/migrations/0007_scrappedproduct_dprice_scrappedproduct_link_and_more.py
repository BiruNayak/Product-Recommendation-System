# Generated by Django 4.0.5 on 2023-01-17 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_delete_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='scrappedproduct',
            name='dprice',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='scrappedproduct',
            name='link',
            field=models.ImageField(default='link', upload_to='image'),
        ),
        migrations.AddField(
            model_name='scrappedproduct',
            name='perdis',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='scrappedproduct',
            name='price',
            field=models.CharField(max_length=50, null=True),
        ),
    ]