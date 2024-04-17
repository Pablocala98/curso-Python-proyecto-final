# Generated by Django 5.0.3 on 2024-04-17 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bookings", "0003_consultorio_rename_detalle_reserva_descripcion_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Masajista",
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
                ("nombre", models.CharField(max_length=50)),
                ("apellido", models.CharField(max_length=50)),
                ("telefono", models.IntegerField(default=None)),
            ],
        ),
        migrations.AlterField(
            model_name="consultorio",
            name="descripcion",
            field=models.TextField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="reserva",
            name="descripcion",
            field=models.TextField(blank=True, max_length=50, null=True),
        ),
    ]