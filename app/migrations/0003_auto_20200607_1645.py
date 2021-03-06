# Generated by Django 3.0.7 on 2020-06-07 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default=None, max_length=255, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='category',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='post_title', to='app.Post'),
        ),
    ]
