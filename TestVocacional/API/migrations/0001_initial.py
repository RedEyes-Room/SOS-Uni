# Generated by Django 2.2.12 on 2020-05-20 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ResponseQuiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=60, verbose_name='email')),
                ('date_test', models.DateTimeField(auto_now_add=True, verbose_name='date test')),
                ('r1', models.IntegerField()),
                ('r2', models.IntegerField()),
                ('r3', models.IntegerField()),
                ('r4', models.IntegerField()),
                ('r5', models.IntegerField()),
                ('r6', models.IntegerField()),
                ('r7', models.IntegerField()),
                ('r8', models.IntegerField()),
                ('r9', models.IntegerField()),
                ('r10', models.IntegerField()),
                ('r11', models.IntegerField()),
                ('r12', models.IntegerField()),
                ('r13', models.IntegerField()),
                ('r14', models.IntegerField()),
                ('r15', models.IntegerField()),
                ('r16', models.IntegerField()),
                ('r17', models.IntegerField()),
                ('r18', models.IntegerField()),
                ('r19', models.IntegerField()),
                ('r20', models.IntegerField()),
                ('r21', models.IntegerField()),
                ('r22', models.IntegerField()),
                ('r23', models.IntegerField()),
                ('r24', models.IntegerField()),
                ('r25', models.IntegerField()),
                ('r26', models.IntegerField()),
                ('r27', models.IntegerField()),
                ('r28', models.IntegerField()),
                ('r29', models.IntegerField()),
                ('r30', models.IntegerField()),
            ],
        ),
    ]
