# Generated by Django 5.0.6 on 2024-07-18 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("student", "0002_rename_code_student_student_code_student_classes_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
    ]
