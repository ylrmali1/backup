# Generated by Django 4.1.7 on 2023-03-24 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_alter_project_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_model',
            field=models.CharField(choices=[('YOLO-V8', 'YOLO-V8'), ('YOLO-V7', 'YOLO-V7'), ('YOLO-V6', 'YOLO-V6'), ('YOLO-V5', 'YOLO-V5')], max_length=20),
        ),
    ]
