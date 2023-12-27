from django.contrib import admin
# from modelsapp.models import student, typeoffields, employee, staff

from modelsapp.models import stud

# # Register your models here.
# class myadmin(admin.ModelAdmin):
#     fields=("Name", "age")

# admin.site.register(student, myadmin)

# # class admin2(admin.ModelAdmin):
# #     fields = ("personal_info", {"fields":('name', 'age')})

# admin.site.register(typeoffields)
    
# # ('Personal info', {'fields': ('first_name', 'last_name')}),

# admin.site.register(employee)
# admin.site.register(staff)

admin.site.register(stud)

admin.site.index_title="ModelsApp Admin"
admin.site.site_header = "MODELS ADMIN"
admin.site.site_title = "MODELSAPP site page"