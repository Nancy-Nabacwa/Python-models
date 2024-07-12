# Generated by Django 5.0.6 on 2024-07-11 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("class_model", "0001_initial"),
        ("course", "0001_initial"),
        ("student", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="student",
            old_name="code",
            new_name="student_code",
        ),
        migrations.AddField(
            model_name="student",
            name="classes",
            field=models.ManyToManyField(
                related_name="students", to="class_model.classroom"
            ),
        ),
        migrations.AddField(
            model_name="student",
            name="courses",
            field=models.ManyToManyField(related_name="students", to="course.course"),
        ),
    ]
