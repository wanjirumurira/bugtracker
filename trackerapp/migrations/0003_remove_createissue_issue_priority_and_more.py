# Generated by Django 4.1.3 on 2022-12-27 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trackerapp', '0002_remove_createissue_issue_screenshort_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='createissue',
            name='issue_priority',
        ),
        migrations.AddField(
            model_name='createissue',
            name='issue_severity',
            field=models.CharField(choices=[('Low Severity', 'Low'), ('Medium Severity', 'Medium '), ('High Severity', 'High')], default='High', max_length=150),
        ),
        migrations.AlterField(
            model_name='createissue',
            name='issue_status',
            field=models.CharField(choices=[('New', 'New'), ('In Progress', 'In Progress'), ('Fixed', 'Fixed'), ('Closed', 'Closed'), ('Reopened', 'Reopened')], default='New', max_length=150),
        ),
    ]
