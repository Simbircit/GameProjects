# Generated by Django 5.1.3 on 2024-11-23 17:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='avatar.png', upload_to='images'),
        ),
        migrations.CreateModel(
            name='GameGenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gameapp.gamepage')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gameapp.genre')),
            ],
        ),
        migrations.AddField(
            model_name='gamepage',
            name='genre',
            field=models.ManyToManyField(blank=True, null=True, through='gameapp.GameGenre', to='gameapp.genre'),
        ),
    ]
