from django.core.management.base import BaseCommand
from datetime import timedelta
from django.utils.timezone import now
from Mucchatlu.models import Thread

class Command(BaseCommand):
    help = 'Deletes threads older than 1 days'

    def handle(self, *args, **kwargs):
        expiration_date = now() - timedelta(days=1)
        deleted, _ = Thread.objects.filter(created_at__lt=expiration_date).delete()
        self.stdout.write(f'{deleted} threads deleted.')
