# Generated by Django 2.2.2 on 2019-06-20 05:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0002_bb_is_activated'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bb',
            options={'get_latest_by': 'published', 'verbose_name': 'Обьявление', 'verbose_name_plural': 'Обьявления'},
        ),
        migrations.AlterOrderWithRespectTo(
            name='bb',
            order_with_respect_to='rubric',
        ),
    ]
