# Generated by Django 5.0.3 on 2024-04-15 20:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0003_category_delete_administrador_alter_blog_cuerpo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(default='Articulo', on_delete=django.db.models.deletion.CASCADE, to='AppBlog.category'),
        ),
    ]