from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from vendor.models import Vendor


class CustomVendorCreationForm(forms.ModelForm):

    class Meta:
        model = Vendor
        fields = ('company_name','status',)

