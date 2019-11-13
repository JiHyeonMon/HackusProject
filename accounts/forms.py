from django import forms
from .models import Member

class MemberFrom(forms.ModelForm):
    class Meta:
        model = Member
        fields = ('id', 'nicname', 'password', 'email', 'interesting')