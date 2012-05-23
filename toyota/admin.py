from toyota.models import Micropage, Event
from django.contrib import admin
from mezzanine.core.admin import DisplayableAdmin

class MicropageAdmin(DisplayableAdmin):

    fieldsets = [
        ("Title",               {'fields': ['title']}),
        ("Published Date",               {'fields': ['publish_date']}),
        ("Published Status",               {'fields': ['status', 'page_type']}),
        ("Header",               {'fields': ['header_top_left', 'header_top_right','header_middle_left', 'header_middle_right']}),
        ("Body",               {'fields': ['body_left_column_top', 'body_left_column_bottom','body_middle_column_top', 'body_middle_column_bottom','body_right_column']}),
        ("Event Details",               {'fields': ['event_details']}),
        ("Footer",               {'fields': ['footer']}),

    ]

    list_display = ('title', 'status', 'publish_date','page_type',)
    list_editable = ('status', 'page_type',)


class EventAdmin(admin.ModelAdmin):
    list_display = ('event', 'location','event_date', 'start_time', 'end_time',)
    list_editable = ('event_date', 'start_time', 'end_time',)

admin.site.register(Micropage, MicropageAdmin)
admin.site.register(Event, EventAdmin)

