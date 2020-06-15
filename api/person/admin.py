from django.contrib import admin
from .models import Person, PersonsAddress, ForbiddenStaff, BorderCrossing


admin.site.register(Person)
admin.site.register(PersonsAddress)
admin.site.register(ForbiddenStaff)
admin.site.register(BorderCrossing)