from django.contrib import admin
from .models import AptiQues
from .models import PersonQues
from .models import JobDetails
from .models import JobRequirement
from .models import PreferredCV
from .models import BaseInfo
# Register your models here.

admin.site.register(AptiQues)
admin.site.register(PersonQues)
admin.site.register(JobDetails)
admin.site.register(JobRequirement)
admin.site.register(PreferredCV)
