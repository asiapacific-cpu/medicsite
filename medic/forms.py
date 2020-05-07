from django import forms

from django.conf import settings
import request

from medic.models import Item




class InquiryForm(forms.Form):
    class Meta:
        fields = ['name','phonenumber','email','message']

class FilterTags(forms.Form):
    tag = forms.ChoiceField()
    class Meta:
        fields = ['tag']