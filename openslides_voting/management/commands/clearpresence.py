from django.core.management.base import BaseCommand

from openslides.users.models import User


class Command(BaseCommand):
    """
    Command to make all users not present.
    """
    help = 'Makes all users not being present.'

    def handle(self, *args, **options):
        n = User.objects.update(is_present=False)
        self.stdout.write('{} users have been set to not being present.'.format(n))
