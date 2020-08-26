from django.contrib import admin
from .models import Form,Section,Field,Choice
# Register your models here.

admin.site.register(Form)
admin.site.register(Section)
admin.site.register(Field)
admin.site.register(Choice)