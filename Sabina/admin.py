from django.contrib import admin

from .models import Parcel, Receiver, Sender

admin.site.register(Sender)
admin.site.register(Receiver)
admin.site.register(Parcel)
