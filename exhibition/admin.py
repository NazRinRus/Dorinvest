from django.contrib import admin
from django.contrib.admin import TabularInline

from exhibition.models import exhibition, participant, partner


##################################################
##### INLINES ####################################
##################################################
class ExhibitionFotoInline(TabularInline):
    model = exhibition.Foto
    fields = ('foto',)


class ParticipantFotoInline(TabularInline):
    model = participant.Avatar
    fields = ('foto',)


class PartnersInline(TabularInline):
    model = exhibition.ExhibitionPartner
    fields = ('partner_id',)


class ParticipantInline(TabularInline):
    model = exhibition.ExhibitionParticipant
    fields = ('participant_id',)


##################################################
##### MODELS #####################################
##################################################
@admin.register(exhibition.Exhibition)
class ExhibitionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'bunner', 'date_begin', 'date_end', 'time_event', 'location', 'venue', 'about')

    inlines = (ExhibitionFotoInline, PartnersInline, ParticipantInline)


@admin.register(exhibition.Foto)
class ExhibitionFotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'foto', 'description',)


@admin.register(participant.Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'color', 'other', 'type_p', 'breed', 'talent', 'avatar_id',)

    inlines = (ParticipantFotoInline,)


@admin.register(participant.TypeParticipant)
class ParticipantTypeAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'sort', 'is_active',)


@admin.register(participant.BreedParticipant)
class ParticipantBreedAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'sort', 'is_active',)


@admin.register(participant.TalentParticipant)
class ParticipantTalentAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'sort', 'is_active',)


@admin.register(participant.Avatar)
class ParticipantBreedAdmin(admin.ModelAdmin):
    list_display = ('id', 'foto', 'description',)


@admin.register(partner.Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'logo', 'info', 'website',)


@admin.register(exhibition.FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'answer',)


@admin.register(exhibition.Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'participant', 'email',)
