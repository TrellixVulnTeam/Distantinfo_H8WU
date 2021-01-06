# Generated by Django 3.1.4 on 2021-01-05 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210104_1239'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название дисциплины')),
            ],
        ),
        migrations.AddField(
            model_name='lecture',
            name='date',
            field=models.DateField(auto_now=True, verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='text',
            field=models.TextField(verbose_name='Текст лекции'),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='title',
            field=models.CharField(max_length=150, verbose_name='Название лекции'),
        ),
        migrations.AddField(
            model_name='lecture',
            name='discipline',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.discipline'),
        ),
    ]
