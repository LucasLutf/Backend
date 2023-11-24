# Generated by Django 4.2.7 on 2023-11-24 18:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Avaliador",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nome", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=100)),
            ],
            options={
                "verbose_name_plural": "Avaliadores",
            },
        ),
    ]