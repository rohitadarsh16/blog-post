# Generated by Django 4.2 on 2023-05-19 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0003_post_img_post_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=20)),
                ('uemail', models.CharField(max_length=20)),
                ('pwd', models.CharField(max_length=20)),
            ],
        ),
    ]