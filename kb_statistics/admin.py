from django.contrib import admin

from django.contrib import admin
from .models import Exercise,Session

# Register your models here.



class ExerciseAdmin(admin.ModelAdmin):
    list_display = ("name", "type")


admin.site.register(Exercise,ExerciseAdmin)


class SessionAdmin(admin.ModelAdmin):
    list_display = ("exercise", "rep_count", "weight", "person", "date")


admin.site.register(Session,SessionAdmin)
