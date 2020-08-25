from django import forms
from .models import Form, Field, Section


class FormForm(forms.ModelForm):
    class Meta:
        model = Form
        fields = ('title','description')


class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ('sec_title','description',)


class FieldForm(forms.ModelForm):
    class Meta:
        model = Field
        fields = ('description','label','field')



