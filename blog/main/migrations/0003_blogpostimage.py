# Generated by Django 4.1 on 2022-08-27 00:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_blogpost_date_updated'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPostImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.ImageField(upload_to='upload_images')),
                ('blogpost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.blogpost')),
            ],
        ),
    ]