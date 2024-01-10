from django.contrib import admin
from .models import Employees, Models, Telephone, Clients, Feedback

admin.site.register(Employees)
admin.site.register(Models)
admin.site.register(Telephone)
admin.site.register(Clients)
admin.site.register(Feedback)