from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from hospital.models import Hospital


class CustomHospitalCreationForm(forms.ModelForm):

    class Meta:
        model = Hospital
        fields = ('hospital_name','registration_no',)

