# Generated by Django 4.1.7 on 2023-03-12 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_task_image_taskimages'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='images/')),
            ],
        ),
        migrations.RenameField(
            model_name='task',
            old_name='image',
            new_name='image_preview',
        ),
        migrations.DeleteModel(
            name='TaskImages',
        ),
        migrations.AddField(
            model_name='images',
            name='post',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.task'),
        ),
    ]
