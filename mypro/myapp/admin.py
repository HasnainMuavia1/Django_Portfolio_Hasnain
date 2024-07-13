from django.contrib import admin
from .models import extend,Skills,Education,Experience,Certifications_license,image
# Register your models here.
admin.site.register(extend)
admin.site.register(Skills)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Certifications_license)
admin.site.register(image)
