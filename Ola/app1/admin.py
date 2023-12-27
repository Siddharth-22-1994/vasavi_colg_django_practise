from django.contrib import admin
from app1.models import employee, std1

# Register your models here.

admin.site.register(employee)

class myadmin(admin.ModelAdmin):
    fields = ["name", ('age', 'place')]
    
admin.site.register(std1, myadmin)

admin.site.index_title = "Ola Admin"
admin.site.site_header="ola admin page"
admin.site.site_title = "ola site title"