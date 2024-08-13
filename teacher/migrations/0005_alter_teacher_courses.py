# Generated by Django 5.0.6 on 2024-08-13 05:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("course", "0002_alter_course_teacher"),
        ("teacher", "0004_teacher_assigned_classrooms_teacher_courses"),
    ]

    operations = [
        migrations.AlterField(
            model_name="teacher",
            name="courses",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="teachers",
                to="course.course",
            ),
        ),
    ]
