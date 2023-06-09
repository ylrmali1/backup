# Generated by Django 4.1 on 2022-10-30 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_alter_trainers_age_alter_trainers_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainers',
            name='age',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='trainers',
            name='description',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='trainers',
            name='image',
            field=models.ImageField(null=True, upload_to='trainers'),
        ),
        migrations.AlterField(
            model_name='trainers',
            name='major',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='trainers',
            name='number',
            field=models.CharField(max_length=11, null=True),
        ),
    ]
