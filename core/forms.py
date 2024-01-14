from django import forms
from .models import EventComment#, NewsPostComment

class EventCommentForm(forms.ModelForm):
  class Meta:
    model = EventComment
    fields = ('name', 'email', 'body')

"""
class NewsPostCommentForm(forms.ModelForm):
  class Meta:
    model = NewsPostComment
    fields = ('name', 'email', 'body')
"""