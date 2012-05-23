from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from toyota.models import Micropage, Event
import logging

logger = logging.getLogger("westerntoyota.custom")

def home(request):
    try:
        home = get_object_or_404(Micropage, page_type='Home')
        events = Event.objects.all().order_by('event_date')
        return render_to_response('index.html',{'home':home, 'events': events,},
                                  context_instance=RequestContext(request))
    except Exception, e:
        logger.error('Error in view: home: {0}'.format(e))


def event_details(request):
    try:
        home = get_object_or_404(Micropage, page_type='Home')
        return render_to_response('event-details.html',{'home':home,},
                                  context_instance=RequestContext(request))
    except Exception, e:
        logger.error('Error in view: event_details: {0}'.format(e))
