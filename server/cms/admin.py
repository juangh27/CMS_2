from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from cms.models import User, Room, Message

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Room)
admin.site.register(Message)
