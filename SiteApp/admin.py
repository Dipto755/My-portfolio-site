from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(ProjectsModel)
admin.site.register(AchievementModel)
admin.site.register(ExperienceModel)
admin.site.register(CertificationModel)