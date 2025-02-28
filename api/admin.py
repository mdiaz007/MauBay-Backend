from django.contrib import admin

# Register your models here.

from .models import active, sold, draft, deleted

admin.site.register(active)
admin.site.register(sold)
admin.site.register(draft)
admin.site.register(deleted)