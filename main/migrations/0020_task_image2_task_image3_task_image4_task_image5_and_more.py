# Generated by Django 4.1.7 on 2023-03-13 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_delete_multipleimage_task_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='image2',
            field=models.ImageField(default='base/PL.png', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='task',
            name='image3',
            field=models.ImageField(default='base/PL.png', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='task',
            name='image4',
            field=models.ImageField(default='base/PL.png', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='task',
            name='image5',
            field=models.ImageField(default='base/PL.png', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='task',
            name='image',
            field=models.ImageField(default='base/PL.png', upload_to='images/'),
        ),
    ]
