from django.contrib import admin

# Register your models here.
from .models import *


class UserAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_time'
    filter_horizontal = ('tag',)
    list_filter = ['category', 'author']
    #显示在后台的数据
    list_display = ('title', 'category', 'author', 'date_time', 'view')


admin.site.register(Article,UserAdmin)

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(UserSheet)


admin.site.site_header = "老飞机的后台"
