# Generated by Django 5.1.7 on 2025-03-23 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_alter_rating_options_rating_comment_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movie',
            options={'ordering': ['-year', 'title']},
        ),
        migrations.RemoveField(
            model_name='movie',
            name='lists',
        ),
        migrations.AddField(
            model_name='movielist',
            name='movies',
            field=models.ManyToManyField(blank=True, related_name='in_lists', to='movies.movie'),
        ),
        migrations.DeleteModel(
            name='UserList',
        ),
    ]
