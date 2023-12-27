from django.contrib import admin
from app1.models import blog, Author, Enrty

# Register your models here.
admin.site.register(blog)
admin.site.register(Author)
admin.site.register(Enrty)