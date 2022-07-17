from django.contrib import admin
from .models import *
# Register your models here.
from .models import QuesModel,Quizes
admin.site.register(QuesModel)
admin.site.register(Quizes)
admin.site.register(Profile)

