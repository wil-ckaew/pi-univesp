# Generated by Django 4.1.2 on 2022-11-05 19:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0023_alter_emprestimos_data_emprestimo'),
    ]

    operations = [
        migrations.AddField(
            model_name='emprestimos',
            name='num_of_livros',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='emprestimos',
            name='data_emprestimo',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 5, 16, 22, 21, 447404)),
        ),
    ]