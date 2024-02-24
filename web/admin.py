from django.contrib import admin
from .models import Owner, Project, Tag

# Register your models here.
admin.site.register(Owner)
admin.site.register(Project)
admin.site.register(Tag)