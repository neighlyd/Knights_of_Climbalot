from django.contrib import admin
from climbalot.models import Monkey, Session, Gym, C_Routes, V_Routes, Y_Routes, Quest
# Register your models here.

admin.site.register(Monkey)
admin.site.register(Session)
admin.site.register(Gym)
admin.site.register(C_Routes)
admin.site.register(V_Routes)
admin.site.register(Y_Routes)
admin.site.register(Quest)
