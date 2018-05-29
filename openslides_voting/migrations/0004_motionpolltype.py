# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-04-03 06:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields
import openslides.utils.models


def add_authorized_voters_object(apps, schema_editor):
    """
    Adds the one and only AuthorizedVoters object.
    """
    model = apps.get_model('openslides_voting', 'AuthorizedVoters')
    # We use bulk_create here because we do not want model's save() method
    # to be called because we do not want our autoupdate signals to be
    # triggered.
    model.objects.bulk_create([model()])


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('motions', '0005_auto_20180202_1318'),
        ('assignments', '0003_candidate_weight'),
        ('openslides_voting', '0003_auto_20180327_1332'),
    ]

    operations = [
        migrations.CreateModel(
            name='VotingToken',
            fields=[
                ('id', models.AutoField(
                    auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=128, unique=True)),
            ],
            options={
                'default_permissions': (),
            },
            bases=(openslides.utils.models.RESTModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='MotionPollType',
            fields=[
                ('id', models.AutoField(
                    auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(
                    choices=[
                        ('analog', 'Analog voting'),
                        ('named_electronic', 'Named electronic voting'),
                        ('token_based_electronic', 'Token-based electronic voting'),
                        ('votecollector', 'Votecollector')],
                    default='analog',
                    max_length=32)),
                ('poll', models.OneToOneField(
                    on_delete=django.db.models.deletion.CASCADE, to='motions.MotionPoll')),
            ],
            options={
                'default_permissions': (),
            },
            bases=(openslides.utils.models.RESTModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='AssignmentPollBallot',
            fields=[
                ('id', models.AutoField(
                    auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', jsonfield.fields.JSONField(default={})),
                ('delegate', models.ForeignKey(
                    blank=True,
                    null=True,
                    on_delete=django.db.models.deletion.CASCADE,
                    to=settings.AUTH_USER_MODEL)),
                ('poll', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='assignments.AssignmentPoll')),
                ('result_token', models.PositiveIntegerField()),
            ],
            options={
                'default_permissions': (),
            },
            bases=(openslides.utils.models.RESTModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='AssignmentPollType',
            fields=[
                ('id', models.AutoField(
                    auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(
                    choices=[
                        ('analog', 'Analog voting'),
                        ('named_electronic', 'Named electronic voting'),
                        ('token_based_electronic', 'Token-based electronic voting'),
                        ('votecollector', 'Votecollector')],
                    default='analog',
                    max_length=32)),
                ('poll', models.OneToOneField(
                    on_delete=django.db.models.deletion.CASCADE, to='assignments.AssignmentPoll')),
            ],
            options={
                'default_permissions': (),
            },
            bases=(openslides.utils.models.RESTModelMixin, models.Model),
        ),
        migrations.AddField(
            model_name='motionpollballot',
            name='result_token',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='motionpollballot',
            name='delegate',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='motionpollballot',
            unique_together=set(),
        ),
        migrations.CreateModel(
            name='AuthorizedVoters',
            fields=[
                ('id', models.AutoField(
                    auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authorized_voters', jsonfield.fields.JSONField(default=[])),
                ('motion_poll', models.OneToOneField(
                    on_delete=django.db.models.deletion.SET_NULL,
                    to='motions.MotionPoll',
                    blank=True,
                    null=True)),
                ('assignment_poll', models.OneToOneField(
                    on_delete=django.db.models.deletion.SET_NULL,
                    to='assignments.AssignmentPoll',
                    blank=True,
                    null=True)),
                ('type', models.CharField(
                    default='analog', max_length=128)),
            ],
            options={
                'default_permissions': (),
            },
            bases=(openslides.utils.models.RESTModelMixin, models.Model),
        ),
        migrations.RenameField(
            model_name='votingcontroller',
            old_name='voters_count',
            new_name='votes_count',
        ),
        migrations.AddField(
            model_name='votingcontroller',
            name='principle',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='openslides_voting.VotingPrinciple'),
        ),
        migrations.AlterModelOptions(
            name='votingcontroller',
            options={
                'default_permissions': (),
                'permissions': (
                    ('can_manage', 'Can manage voting'),
                    ('can_see_token_voting', 'Can see the token voting interface')
                )
            },
        ),
        migrations.CreateModel(
            name='AssignmentAbsenteeVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.CharField(max_length=255)),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assignments.Assignment')),
                ('delegate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'default_permissions': (),
            },
            bases=(openslides.utils.models.RESTModelMixin, models.Model),
        ),
        migrations.AlterUniqueTogether(
            name='assignmentabsenteevote',
            unique_together=set([('assignment', 'delegate')]),
        ),
        migrations.RenameModel(
            old_name='AbsenteeVote',
            new_name='MotionAbsenteeVote',
        ),
        migrations.RunPython(
                add_authorized_voters_object
        ),
    ]