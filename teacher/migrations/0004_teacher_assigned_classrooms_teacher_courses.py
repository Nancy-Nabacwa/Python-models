# Generated by Django 5.0.6 on 2024-08-13 04:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("class_model", "0003_remove_classroom_teachers_and_more"),
        ("course", "0002_alter_course_teacher"),
        ("teacher", "0003_alter_teacher_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="teacher",
            name="assigned_classrooms",
            field=models.ManyToManyField(
                related_name="teachers_assigned", to="class_model.classroom"
            ),
        ),
        migrations.AddField(
            model_name="teacher",
            name="courses",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="teachers",
                to="course.course",
            ),
        ),
    ]
