from django.core.management.base import BaseCommand, CommandError
from toyota.models import Event
from datetime import datetime
import logging

logger = logging.getLogger("westerntoyota.custom")

class Command(BaseCommand):
    help = 'Deletes Expired Events'
    def handle(self, *args, **options):
        try:
            logger.debug('Starting deletion of expired events.')
            expired_events = Event.objects.filter(event_date__lt=datetime.now())
            for ee in expired_events:
                logger.debug('Deleting Expired Events {0} Date {1}'.format(ee.event, ee.event_date))
                ee.delete()

        except Exception, e:
            logger.error('Error deleting expired events: {0}'.format(e))
  