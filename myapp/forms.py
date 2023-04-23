from django import forms
from .models import musicDatabased
class Post(forms.ModelForm):
  class Meta:
    model = musicDatabased
    fields = '__all__'