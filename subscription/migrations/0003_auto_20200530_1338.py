# Generated by Django 3.0.6 on 2020-05-30 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_auto_20200530_1338'),
        ('users', '0004_auto_20200530_1338'),
        ('subscription', '0002_subscription_subscribers'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subscription',
            options={'ordering': ('date_subscribed',), 'verbose_name_plural': 'Subscriptions'},
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='subscribers',
        ),
        migrations.AddField(
            model_name='subscription',
            name='courses',
            field=models.ManyToManyField(related_name='subscribers', to='course.Course'),
        ),
        migrations.AddField(
            model_name='subscription',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='subscription',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.StudentProfile'),
        ),
        migrations.AddField(
            model_name='subscription',
            name='students',
            field=models.ManyToManyField(blank=True, null=True, related_name='my_subscriptions', to='users.StudentProfile'),
        ),
    ]