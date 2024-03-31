from django.contrib import admin
from exhibition.models import exhibition, participant, partner

@admin.register(exhibition.Exhibition)
class ExhibitionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'bunner', 'date', 'location',)

@admin.register(exhibition.Foto)
class ExhibitionFotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'foto', 'description',)

@admin.register(participant.Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'color', 'other', 'type_p', 'breed', 'avatar_id',)

@admin.register(participant.TypeParticipant)
class ParticipantTypeAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'sort', 'is_active',)

@admin.register(participant.BreedParticipant)
class ParticipantBreedAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'sort', 'is_active',)

@admin.register(participant.Avatar)
class ParticipantBreedAdmin(admin.ModelAdmin):
    list_display = ('id', 'foto', 'description',)

@admin.register(partner.Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'logo', 'info', 'website',)