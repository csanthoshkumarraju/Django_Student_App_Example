# Generated by Django 5.0.7 on 2024-07-21 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_student', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='educationdetail',
            name='goals',
        ),
        migrations.RemoveField(
            model_name='educationdetail',
            name='homework',
        ),
        migrations.AddField(
            model_name='educationdetail',
            name='Education_Btech_Degree_College_Grade',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='educationdetail',
            name='Education_Btech_Degree_College_Location',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='educationdetail',
            name='Education_Btech_Degree_College_Name',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='educationdetail',
            name='Education_Inter_College_Grade',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='educationdetail',
            name='Education_Inter_College_Location',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='educationdetail',
            name='Education_Inter_College_Name',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='educationdetail',
            name='Education_SSC_School_Name',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='educationdetail',
            name='Education_SSC_school_Grade',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='educationdetail',
            name='Education_SSC_school_Location',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='educationdetail',
            name='Future_goal_plans',
            field=models.TextField(max_length=100000, null=True),
        ),
        migrations.AddField(
            model_name='educationdetail',
            name='Future_goal_plans_completed',
            field=models.TextField(max_length=100000, null=True),
        ),
        migrations.AddField(
            model_name='educationdetail',
            name='Today_homework_completed',
            field=models.TextField(max_length=100000, null=True),
        ),
        migrations.AddField(
            model_name='educationdetail',
            name='Today_homework_todo',
            field=models.TextField(max_length=100000, null=True),
        ),
    ]
