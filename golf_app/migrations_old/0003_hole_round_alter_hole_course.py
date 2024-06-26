# Generated by Django 4.2.13 on 2024-06-11 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('golf_app', '0002_alter_round_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='hole',
            name='round',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='holes', to='golf_app.round'),
        ),
        migrations.AlterField(
            model_name='hole',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='holes', to='golf_app.course'),
        ),
    ]
