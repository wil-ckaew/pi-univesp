# Generated by Django 4.1.2 on 2022-11-05 19:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0024_emprestimos_num_of_livros_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimos',
            name='data_emprestimo',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 5, 16, 22, 45, 583797)),
        ),
    ]
