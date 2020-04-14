# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-09-18 19:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields
import openslides.utils.models
import openslides_voting.models


def add_authorized_voters_object(apps, schema_editor):
    """
    Adds the one and only AuthorizedVoters object.
    """
    model = apps.get_model('openslides_voting', 'AuthorizedVoters')
    # We use bulk_create here because we do not want model's save() method
    # to be called because we do not want our autoupdate signals to be
    # triggered.
    model.objects.bulk_create([model()])

def add_voting_controller_object(apps, schema_editor):
    """
    Adds the VotingController object.
    """
    model = apps.get_model('openslides_voting', 'VotingController')
    model.objects.bulk_create([model()])


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('motions', '0010_auto_20180822_1042'),
        ('assignments', '0005_auto_20180822_1042'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
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
        migrations.CreateModel(
            name='AssignmentPollBallot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', jsonfield.fields.JSONField(default={})),
                ('device', models.CharField(max_length=32, null=True)),
                ('result_token', models.PositiveIntegerField()),
                ('is_dummy', models.BooleanField(default=False)),
                ('delegate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assignments.AssignmentPoll')),
            ],
            options={
                'default_permissions': (),
            },
            bases=(openslides.utils.models.RESTModelMixin, models.Model, openslides_voting.models.PollBallot),
        ),
        migrations.CreateModel(
            name='AssignmentPollType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('analog', 'Analog voting'), ('named_electronic', 'Named electronic voting'), ('token_based_electronic', 'Token-based electronic voting'), ('votecollector', 'VoteCollector default (personalized and active keypads only, with single votes)'), ('votecollector_secret', 'VoteCollector secret (no single votes and delegate board)'), ('votecollector_pseudo_secret', 'VoteCollector grey (no single votes, only grey seats on delegate board)'), ('votecollector_anonymous', 'VoteCollector anonymous (anonymous and personalized keypads, with single votes, no delegate board)')], default='analog', max_length=32)),
                ('poll', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='assignments.AssignmentPoll')),
            ],
            options={
                'default_permissions': (),
            },
            bases=(openslides.utils.models.RESTModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='AttendanceLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', jsonfield.fields.JSONField()),
                ('created', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created'],
                'default_permissions': (),
            },
            bases=(openslides.utils.models.RESTModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='AuthorizedVoters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authorized_voters', jsonfield.fields.JSONField(default=[])),
                ('type', models.CharField(default='', max_length=128)),
                ('assignment_poll', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='assignments.AssignmentPoll')),
                ('motion_poll', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='motions.MotionPoll')),
            ],
            options={
                'default_permissions': (),
            },
            bases=(openslides.utils.models.RESTModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Keypad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(unique=True)),
                ('battery_level', models.SmallIntegerField(default=-1)),
                ('in_range', models.BooleanField(default=False)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'default_permissions': (),
            },
            bases=(openslides.utils.models.RESTModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='MotionAbsenteeVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.CharField(max_length=1)),
                ('delegate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('motion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='motions.Motion')),
            ],
            options={
                'default_permissions': (),
            },
            bases=(openslides.utils.models.RESTModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='MotionPollBallot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.CharField(blank=True, max_length=1)),
                ('device', models.CharField(max_length=32, null=True)),
                ('result_token', models.PositiveIntegerField()),
                ('is_dummy', models.BooleanField(default=False)),
                ('delegate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='motions.MotionPoll')),
            ],
            options={
                'default_permissions': (),
            },
            bases=(openslides.utils.models.RESTModelMixin, models.Model, openslides_voting.models.PollBallot),
        ),
        migrations.CreateModel(
            name='MotionPollType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('analog', 'Analog voting'), ('named_electronic', 'Named electronic voting'), ('token_based_electronic', 'Token-based electronic voting'), ('votecollector', 'VoteCollector default (personalized and active keypads only, with single votes)'), ('votecollector_secret', 'VoteCollector secret (no single votes and delegate board)'), ('votecollector_pseudo_secret', 'VoteCollector grey (no single votes, only grey seats on delegate board)'), ('votecollector_anonymous', 'VoteCollector anonymous (anonymous and personalized keypads, with single votes, no delegate board)')], default='analog', max_length=32)),
                ('poll', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='motions.MotionPoll')),
            ],
            options={
                'default_permissions': (),
            },
            bases=(openslides.utils.models.RESTModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='VotingController',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_status', models.CharField(default='No device', max_length=200)),
                ('voting_mode', models.CharField(max_length=50, null=True)),
                ('voting_target', models.IntegerField(default=0)),
                ('voting_duration', models.IntegerField(default=0)),
                ('votes_count', models.IntegerField(default=0)),
                ('votes_received', models.IntegerField(default=0)),
                ('is_voting', models.BooleanField(default=False)),
            ],
            options={
                'permissions': (('can_manage', 'Can manage voting'), ('can_see_token_voting', 'Can see the token voting interface'), ('can_vote', 'Can vote')),
                'default_permissions': (),
            },
            bases=(openslides.utils.models.RESTModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='VotingPrinciple',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('decimal_places', models.PositiveIntegerField()),
                ('assignments', openslides_voting.models.OneToManyField(blank=True, to='assignments.Assignment')),
                ('motions', openslides_voting.models.OneToManyField(blank=True, to='motions.Motion')),
            ],
            options={
                'default_permissions': (),
            },
            bases=(openslides.utils.models.RESTModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='VotingProxy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delegate', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('proxy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mandates', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'default_permissions': (),
            },
            bases=(openslides.utils.models.RESTModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='VotingShare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shares', models.DecimalField(decimal_places=6, max_digits=15)),
                ('delegate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shares', to=settings.AUTH_USER_MODEL)),
                ('principle', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='openslides_voting.VotingPrinciple')),
            ],
            options={
                'default_permissions': (),
            },
            bases=(openslides.utils.models.RESTModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='VotingToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=128, unique=True)),
            ],
            options={
                'default_permissions': (),
            },
            bases=(openslides.utils.models.RESTModelMixin, models.Model),
        ),
        migrations.AddField(
            model_name='votingcontroller',
            name='principle',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='openslides_voting.VotingPrinciple'),
        ),
        migrations.AlterUniqueTogether(
            name='votingshare',
            unique_together=set([('delegate', 'principle')]),
        ),
        migrations.AlterUniqueTogether(
            name='motionabsenteevote',
            unique_together=set([('motion', 'delegate')]),
        ),
        migrations.AlterUniqueTogether(
            name='assignmentabsenteevote',
            unique_together=set([('assignment', 'delegate')]),
        ),
        migrations.RunPython(
            add_authorized_voters_object
        ),
        migrations.RunPython(
            add_voting_controller_object
        ),
    ]
