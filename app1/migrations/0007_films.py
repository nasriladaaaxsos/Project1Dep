# Generated by Django 3.2.16 on 2022-12-16 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_movie_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Films',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=45)),
                ('description', models.TextField()),
                ('release_date', models.DateTimeField()),
                ('duration', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ManyToManyField(related_name='films', to='app1.User')),
            ],
        ),
    ]
