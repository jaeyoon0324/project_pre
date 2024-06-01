# Generated by Django 5.0.6 on 2024-06-01 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0006_alter_post_url_alter_post_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='CrawledData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('url', models.URLField()),
                ('content', models.TextField()),
            ],
        ),
    ]