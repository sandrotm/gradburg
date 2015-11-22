from django.contrib import admin

from .models import Page, Flat, FlatType, Image


class FlatAdmin(admin.ModelAdmin):
    list_display = ('presented', 'status')


class FlatTypeAdmin(admin.ModelAdmin):
    list_display = ('title', )


class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', )


admin.site.register(Page)
admin.site.register(Flat, FlatAdmin)
admin.site.register(FlatType, FlatTypeAdmin)
admin.site.register(Image, ImageAdmin)
