from django.contrib import admin

from users.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'cell_phone_number', 'student_number', 'image')


admin.site.register(Profile, ProfileAdmin)
