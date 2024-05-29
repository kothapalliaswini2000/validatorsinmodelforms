from django import forms
from.models import *
from django.core import validators

class TopicForm(forms.ModelForm):
    mobileno=forms.CharField(min_length=10,max_length=10,validators=[validators.RegexValidator('[6-9]\d{9}')])
    class Meta:
        model=Topic
        fields='__all__'

class WebpageForm(forms.ModelForm):
    reemail=forms.EmailField()
    # botcatcher=forms.CharField(widget=forms.HiddenInput,required=False)
    class Meta:
        model=Webpage
        fields='__all__'
    # def clean_botcatcher(self):
    #     cu=self.cleaned_data['botcahtcher']
    #     if len(cu)>0:
    #         raise forms.ValidationError('Invalid')
    def clean(self):
        e=self.cleaned_data['email']
        re=self.cleaned_data['reemail']
        if e!=re:
            raise forms.ValidationError('email doesnot match with reemail')
        
class AccessRecordForm(forms.ModelForm):
    class Meta:
        model=AccessRecord
        fields='__all__'

    
    


    
