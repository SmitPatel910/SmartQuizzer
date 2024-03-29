# Generated by Django 3.0.5 on 2021-05-05 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0006_auto_20210505_0937'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='que_pic',
            field=models.ImageField(blank=True, null=True, upload_to='que_pic/Question/'),
        ),
        migrations.AlterField(
            model_name='course',
            name='quiz_status',
            field=models.CharField(choices=[('Upcoming', 'Upcoming')], default='Upcoming', max_length=12),
        ),
    ]
