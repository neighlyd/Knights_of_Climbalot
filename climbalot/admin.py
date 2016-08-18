from django.contrib import admin
from climbalot.models import Monkey, Session, Gym, C_Routes, V_Routes, Y_Routes, Quest
# Register your models here.

'''
# This function automates the creation of inline instances to feed into the main class.
# However, I can not figure out how to append the "classes = ('collapse', )" argument to it, allowing it to collapse in the admin view.
def get_inline_model(m):
    return type(
        'DynamicInline',
        (admin.TabularInline, ),
        {'model': m}
    )
'''

class VInline(admin.TabularInline):
    model = V_Routes
    classes = ('collapse',)

class CInline(admin.TabularInline):
    model = C_Routes
    classes = ('collapse',)

class YInline(admin.TabularInline):
    model = Y_Routes
    classes = ('collapse',)

class SessionViewer(admin.ModelAdmin):
    inlines = (
        CInline,
        VInline,
        YInline,
    )

admin.site.register(Monkey)
admin.site.register(Session, SessionViewer)
admin.site.register(Gym)
admin.site.register(Quest)
