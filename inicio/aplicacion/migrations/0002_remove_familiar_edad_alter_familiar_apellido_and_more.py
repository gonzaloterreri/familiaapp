# Generated by Django 4.0.5 on 2022-06-14 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='familiar',
            name='edad',
        ),
        migrations.AlterField(
            model_name='familiar',
            name='apellido',
            field=models.CharField(max_length=20, verbose_name='Apellido'),
        ),
        migrations.AlterField(
            model_name='familiar',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='familiar',
            name='nacimiento',
            field=models.DateTimeField(verbose_name='Nacimiento'),
        ),
        migrations.AlterField(
            model_name='familiar',
            name='nombre',
            field=models.CharField(max_length=20, verbose_name='Nombre'),
        ),
    ]
