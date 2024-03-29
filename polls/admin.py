from django.contrib import admin
from polls.models import Choice, Poll  

# Register your models here.

class ChoiceInLine(admin.StackedInline):
  model = Choice
  extra = 3
  
class PollAdmin(admin.ModelAdmin):
  fieldsets = [
    (None,               {'fields': ['question_text']}),
    ('Date Information', {'fields': ['pub_date'],
                          'classes': ['collapse']}),
  ]
  inlines = [ChoiceInLine]
  
admin.site.register(Poll, PollAdmin)
  