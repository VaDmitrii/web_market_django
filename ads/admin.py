from django.contrib import admin

from ads.models import Ad, Category, Selection

admin.site.register(Category)
admin.site.register(Ad)
admin.site.register(Selection)
