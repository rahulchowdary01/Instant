# Generated by Django 4.1.2 on 2022-10-21 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0003_sproduct"),
    ]

    operations = [
        migrations.RenameField(
            model_name="sproduct", old_name="image", new_name="image1",
        ),
        migrations.AddField(
            model_name="sproduct",
            name="image2",
            field=models.ImageField(null=True, upload_to=""),
        ),
        migrations.AddField(
            model_name="sproduct",
            name="image3",
            field=models.ImageField(null=True, upload_to=""),
        ),
    ]