# Generated by Django 3.2.9 on 2022-01-29 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_useraccount_introduction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='image',
            field=models.ImageField(default='images/default.png', upload_to='images', verbose_name='プロフィール画像'),
        ),
    ]