# Generated by Django 5.0.6 on 2024-07-12 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("class_model", "0001_initial"),
        ("course", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ClassPeriod",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("start_time", models.TimeField()),
                ("end_time", models.TimeField()),
                ("day_of_week", models.DateField()),
                (
                    "classrooms",
                    models.ManyToManyField(
                        related_name="class_periods", to="class_model.classroom"
                    ),
                ),
                (
                    "courses",
                    models.ManyToManyField(
                        related_name="class_periods", to="course.course"
                    ),
                ),
            ],
        ),
    ]
