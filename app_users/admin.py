from django.contrib import admin
from .models import Profile, MedicalHistory

class MedicalHistoryInline(admin.TabularInline):
    model = MedicalHistory
    extra = 1  # Number of empty forms to display

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'birthdate', 'address', 'weight', 'height', 'exercise_level')
    search_fields = ('user__username', 'user__email', 'address')
    list_filter = ('exercise_level', 'birthdate')
    ordering = ('user', 'birthdate')
    inlines = [MedicalHistoryInline]  # Include the MedicalHistory inline

@admin.register(MedicalHistory)
class MedicalHistoryAdmin(admin.ModelAdmin):
    list_display = ('profile', 'item')
    search_fields = ('profile__user__username', 'item')
