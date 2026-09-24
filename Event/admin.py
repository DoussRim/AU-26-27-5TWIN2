from django.contrib import admin
from Event.models import *
# Register your models here.
class FilterDate(admin.SimpleListFilter):
    title="Event Date"
    parameter_name="evt_date"
    def lookups(self, request, model_admin):
        return (
                ('PE',('Past Event(s)')),
                ('UE',('Upcoming Event(s)')),
                ('TE',('Today Event(s)')),
                )
    def queryset(self, request, queryset):
        if self.value()=="PE":
            return queryset.filter(evt_date__lt=datetime.now())
        if self.value()=="UE":
                    return queryset.filter(evt_date__gt=datetime.now())
        if self.value()=="TE":
                    return queryset.filter(evt_date__exact=datetime.now())
class ParticipantAdmin(admin.TabularInline):
    model=Participants
    extra=1
    readonly_fields=('participation_date')
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display=('title','category','description','evt_date',
                  'creation_date','update_date','organizer',
                  'list_participant','state')
    def list_participant(self,obj):
        names=[p.username for p in obj.participant.all()]
        result=";".join(names[:2])
        if not names:
            return " No Participants !"
        return result + (f"({+len(names-2)}) more" if len(names)>2 else "")
    autocomplete_fields=['organizer']
    readonly_fields=['creation_date','update_date']
    fieldsets=(
        ('A propos',{
            'fields':('title','description','category','image','nb_participant')
        }),
        ('Etat',{
                    'fields':('state',)
                }),
        ('Event Dates',{
                    'fields':('evt_date','creation_date','update_date')
                }),
        (None,{
                            'fields':('organizer',)
                        }),
        
    )
    list_per_page=2
    search_fields=['title','category']
    list_filter=['title','organizer',FilterDate]
    inlines=[ParticipantAdmin]

#admin.site.register(Event,EventAdmin)