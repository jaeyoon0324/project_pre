# Generated by Django 5.0.6 on 2024-06-01 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0007_crawleddata'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('url', models.URLField()),
            ],
        ),
        migrations.DeleteModel(
            name='CrawledData',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
