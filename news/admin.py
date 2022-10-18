from django.contrib import admin
from news.models import GalleryModel, NewsModel, EventModel
# from modeltranslation.admin import TranslationAdmin
#
#
# admin.site.register(NewsModel)
# admin.site.register(GalleryModel)
# admin.site.register(EventModel)


#
# class MyTranslationAdmin(TranslationAdmin):
#     class Media:
#         js = (
#             'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
#             'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
#             'modeltranslation/js/tabbed_translation_fields.js',
#         )
#         css = {
#             'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
#         }
#
#
# @admin.register(GalleryModel)
# class GalleryModelAdmin(MyTranslationAdmin):
#     list_display = ['title']
#     list_filter = ['title']
#     search_fields = ['title']
#
#
# @admin.register(NewsModel)
# class NewsModelAdmin(MyTranslationAdmin):
#     list_display = ['title', 'content']
#     list_filter = ['title']
#     search_fields = ['date']
#
#
# @admin.register(EventModel)
# class EventModelAdmin(MyTranslationAdmin):
#     list_display = ['title', 'content']
#     list_filter = ['title']
#     search_fields = ['date']

