# Generated by Django 4.1.7 on 2023-03-13 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_remove_task_image_alter_multipleimage_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='multipleimage',
            name='images',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
