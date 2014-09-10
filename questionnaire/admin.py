from django.contrib import admin

from .models import *


admin.site.register(Questionnaire)
admin.site.register(Question)
admin.site.register(Option)
admin.site.register(Response)
admin.site.register(Done)
admin.site.register(DoneAnswer)