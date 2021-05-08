from django.contrib import admin
from .models import Question , Choice

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date' , 'question_text']
    list_display = ('pub_date' , 'question_text','was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    inlines = [ChoiceInLine]
admin.site.register(Question , QuestionAdmin)

# Register your models here.
